#Main responsibilities:

#     Get today's price from MarketData

#     Get a decision (buy/sell/hold with amount) , validated from decisionhandler

#     Call CurrencyConverter

#     Update the portfolio

#     Advance the day and loop or finish when done

#     Maybe: Get HistoryTracker / PerformanceReporter

#     Later: Visualize in graph


from marketdataloader import MarketDataLoader
from decisionhandler import DecisionHandler, Decision
from portfolio import Currency, Portfolio
from datacleaner import DataCleaner, CleanRow
from gamesetup import GameSetup
from portfolio import Portfolio, Currency
class GameController():
    def __init__(self, game_day:int, market_data: MarketDataLoader):
        self.gameday = game_day
        self.marketdata = market_data

    def _advance_game_day(self):
        self.gameday += 1
        if self.gameday == len(self.marketdata):
            return "DONE"

    def _get_todays_prices(self, game_day) -> CleanRow:        
        return self.marketdata[game_day]
    
    def _get_todays_decision(self):
        return ("buy", 100.0, Currency.BTC)
    
    def _validate_decision(self, amount, currency_to_spend:Currency, portfolio: Portfolio):
        return DecisionHandler.handle(amount, currency_to_spend, portfolio)
    
    def _update_portfolio(self, portfolio):
        # decision = self._validate_decision()
        # if decision.validity:
        portfolio.add("100", Currency.BTC)
        

game_length = int(3)
clean_data = DataCleaner("data/btc_historical_data.csv").clean_csv()
#multi-currency support?
seed = GameSetup(clean_data, game_length).generate_seed()
market_data = MarketDataLoader(clean_data, seed, game_length).load()
print(f"Market Data: {market_data}")
portfolio = Portfolio()
portfolio.add(100, Currency.USD)
game_controller = GameController(0, market_data)
for day in range(1,len(market_data)):
    print(f"Day: {day}")
    day_prices = game_controller._get_todays_prices(day)
    day_decision = game_controller._update_portfolio(portfolio)
    game_controller._advance_game_day()
    print(portfolio.balance)


