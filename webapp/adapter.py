# webapp/adapter.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from typing import Dict, Any, List
from datacleaner import DataCleaner
from stock_data import match_dates
from gamesetup import GameSetup
from marketdataloader import MarketDataLoader
from portfolio import Portfolio
from currencyconverter import CurrencyConverter
from enums import Action, Currency
from history_tracker import HistoryTracker

def _coerce(params: Dict[str, Any]):
    gl = int(params.get("game_length", 100))
    ss = int(params.get("step_size", 1))
    sd = params.get("seed")
    sd = None if sd in (None, "", "null") else int(sd)
    return gl, ss, sd

def _aligned_btc():
    cleaner = DataCleaner()
    btc = cleaner.clean_csv("data/btc_historical_data.csv")
    spx = cleaner.clean_csv("data/sp500_historical_data.csv")
    btc_aligned, _ = match_dates(spx, btc)  # returns (btc, spx)
    return btc_aligned

def run_preview(params: Dict[str, Any]) -> Dict[str, Any]:
    gl, ss, sd = _coerce(params)
    btc = _aligned_btc()
    setup = GameSetup(btc, gl, ss)
    chosen_seed = setup.seed if sd is None else sd
    loader = MarketDataLoader(chosen_seed, gl, ss)
    series = loader.load(btc)
    first, last = series[0], series[-1]
    return {
        "ok": True,
        "seed": chosen_seed,
        "game_length": gl,
        "step_size": ss,
        "start_date": first.date.isoformat(),
        "end_date": last.date.isoformat(),
        "start_price": first.close_price,
        "end_price": last.close_price,
        "points": len(series),
    }

def get_series_prices(params: Dict[str, Any]) -> List[float]:
    gl, ss, sd = _coerce(params)
    btc = _aligned_btc()
    setup = GameSetup(btc, gl, ss)
    chosen_seed = setup.seed if sd is None else sd
    loader = MarketDataLoader(chosen_seed, gl, ss)
    series = loader.load(btc)
    return [row.close_price for row in series]

def start_game(params: Dict[str, Any]) -> Dict[str, Any]:
    gl, ss, sd = _coerce(params)
    btc = _aligned_btc()
    setup = GameSetup(btc, gl, ss)
    chosen_seed = setup.seed if sd is None else sd
    loader = MarketDataLoader(chosen_seed, gl, ss)
    series = loader.load(btc)

    state = {
        "seed": chosen_seed,
        "game_length": gl,
        "step_size": ss,
        "day_idx": 0,
        "series": series,  # list[CleanRow]
        "portfolio": {"USD": 1000.0, "BTC": 0.0, "ETH": 0.0},  # flat dict for serialization
    }
    return _public_state(state)

# keep imports as you have them

# --- helpers for portfolio (unchanged) ---
def _rehydrate_portfolio(state) -> Portfolio:
    b = state["portfolio"]
    return Portfolio(
        start_money=0,
        balance={
            Currency.USD: float(b.get("USD", 0.0)),
            Currency.BTC: float(b.get("BTC", 0.0)),
            Currency.ETH: float(b.get("ETH", 0.0)),
        },
    )

def _persist_portfolio(state, p: Portfolio):
    bal = p.get_all_balances()
    state["portfolio"] = {
        "USD": bal[Currency.USD],
        "BTC": bal[Currency.BTC],
        "ETH": bal[Currency.ETH],
    }

def _mark_to_market(state: Dict[str, Any]) -> float:
    p = _rehydrate_portfolio(state)
    conv = CurrencyConverter()
    day = min(state["day_idx"], len(state["series"]) - 1)
    price = state["series"][day]
    bal = p.get_all_balances()
    usd = bal[Currency.USD]
    btc_usd = conv.convert(bal[Currency.BTC], Currency.BTC, Currency.USD, price)
    return round(usd + btc_usd, 2)

# --- public view (no internals like series) ---
def public_view(state: Dict[str, Any]) -> Dict[str, Any]:
    first = state["series"][0]
    last = state["series"][-1]
    idx = state["day_idx"]
    cur = state["series"][min(idx, len(state["series"]) - 1)]
    finished = idx >= len(state["series"])
    payload = {
        "ok": True,
        "seed": state["seed"],
        "day": idx,
        "start_date": first.date.isoformat(),
        "end_date": last.date.isoformat(),
        "current_date": cur.date.isoformat(),
        "current_price": cur.close_price,
        "portfolio": state["portfolio"],
        "portfolio_value_usd": _mark_to_market(state),
        "finished": finished,
        "message": state.get("last_message", ""),
    }
    if finished:
        payload["report"] = _build_report(state)
    return payload


# --- game lifecycle ---
def start_game(params: Dict[str, Any]) -> Dict[str, Any]:
    gl, ss, sd = _coerce(params)

    # load and align full datasets once
    btc_full = _aligned_btc()
    cleaner = DataCleaner()
    spx_full =cleaner.clean_csv("data/sp500_historical_data.csv")
    # align again to ensure same dates order as btc_full
    _, spx_full_aligned = match_dates(spx_full, btc_full)

    setup = GameSetup(btc_full, gl, ss)
    chosen_seed = setup.seed if sd is None else sd
    loader = MarketDataLoader(chosen_seed, gl, ss)

    btc_series = loader.load(btc_full)
    spx_series = loader.load(spx_full_aligned)

    state = {
        "seed": chosen_seed,
        "game_length": gl,
        "step_size": ss,
        "day_idx": 1,
        "events": [],
        "series": btc_series,
        "sp_series": spx_series,
        "btc_full_last": btc_full[-1],
        "spx_full_last": spx_full_aligned[-1],
        "initial_value": 1000.0,
        "portfolio": {"USD": 1000.0, "BTC": 0.0, "ETH": 0.0},
        "actions": [],                     # ← new
    }
    return state


def apply_action(state: dict, action_str: str) -> dict:
    action = Action[action_str.upper()] if action_str else Action.HOLD
    day = state["day_idx"]
    if day >= len(state["series"]):
        state["last_message"] = "game finished"
        return state

    price = state["series"][day]
    p = _rehydrate_portfolio(state)
    ok = True
    msg = "hold"

    try:
        if action == Action.BUY:
            ok = p.handle_transaction(Action.BUY, price)
            msg = "bought all USD to BTC" if ok else "no USD to convert"
        elif action == Action.SELL:
            ok = p.handle_transaction(Action.SELL, price)
            msg = "sold all BTC to USD" if ok else "no BTC to convert"
        else:
            msg = "hold"
    except ValueError as e:
        ok = False
        msg = str(e)

    if ok:
        # advance one day
        state["day_idx"] = day + 1
        # record marker only for successful BUY/SELL
        if action in (Action.BUY, Action.SELL):
            state["events"].append({"i": day, "action": action.name})

    _persist_portfolio(state, p)
    state["last_message"] = msg
    return state



def _build_report(state: Dict[str, Any]) -> Dict[str, float]:
    # current portfolio value in USD
    current_val = _mark_to_market(state)

    # rehydrate Portfolio
    p = _rehydrate_portfolio(state)

    # use your tracker with BTC slice, SPX slice, initial, portfolio, and last full-day prices
    tracker = HistoryTracker(
        crypto_market_data=state["series"],
        market_data_sp=state["sp_series"],
        initial_portfolio_value=float(state["initial_value"]),
        portfolio=p,
        last_btc_data_entry=state["btc_full_last"],
        last_sp_data_entry=state["spx_full_last"],
    )
    r = tracker.generate_report()
    return {
        "buy_hold_gain_btc_pct": r.buy_hold_gain,
        "user_gain_pct": r.user_gain,
        "buy_hold_gain_spx_pct": r.stock_gain,
        "bogle_btc_gain_pct": r.bogle_btc_gain,
        "bogle_spx_gain_pct": r.bogle_stock_gain,
        "current_portfolio_value_usd": round(current_val, 2),
    }