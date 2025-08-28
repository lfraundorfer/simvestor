# webapp/adapter.py

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from typing import Dict, Any
from datacleaner import DataCleaner
from stock_data import match_dates
from gamesetup import GameSetup
from marketdataloader import MarketDataLoader

def run_preview(params: Dict[str, Any]) -> Dict[str, Any]:
    # Coerce with defaults, no core edits
    game_length = int(params.get("game_length", 100))
    step_size = int(params.get("step_size", 1))
    seed = params.get("seed")
    seed = None if seed in (None, "", "null") else int(seed)

    # Load datasets from existing CSVs
    cleaner = DataCleaner()
    btc = cleaner.clean_csv("data/btc_historical_data.csv")
    spx = cleaner.clean_csv("data/sp500_historical_data.csv")

    # Align dates using your existing helper
    btc_aligned, spx_aligned = match_dates(spx, btc)  # returns (btc, spx)

    # Pick BTC path for now. No changes to gamecontroller yet.
    setup = GameSetup(btc_aligned, game_length, step_size)
    chosen_seed = setup.seed if seed is None else seed
    loader = MarketDataLoader(chosen_seed, game_length, step_size)
    series = loader.load(btc_aligned)

    first = series[0]
    last = series[-1]

    return {
        "ok": True,
        "seed": chosen_seed,
        "game_length": game_length,
        "step_size": step_size,
        "start_date": first.date.isoformat(),
        "end_date": last.date.isoformat(),
        "start_price": first.close_price,
        "end_price": last.close_price,
        "points": len(series),
    }
