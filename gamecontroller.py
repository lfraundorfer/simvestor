#Main responsibilities:

#     Get today's price from MarketData

#     Get a decision (buy/sell/hold with amount) , validated from decisionhandler

#     Call CurrencyConverter

#     Update the portfolio

#     Advance the day and loop or finish when done

#     Maybe: Get HistoryTracker / PerformanceReporter

#     Later: Visualize in graph


from marketdataloader import MarketDataLoader
from portfolio import Portfolio
from datacleaner import DataCleaner, CleanRow
from gamesetup import GameSetup
from user_input_parser import get_user_input, Action
from history_tracker import HistoryTracker
from stock_data import match_dates




class GameController():
    def __init__(self, game_day:int, market_data: list, portfolio: Portfolio):
        self.gameday = game_day or 1
        self.marketdata = market_data
        self.portfolio = portfolio

    def _advance_game_day(self):
        self.gameday += 1
        if self.gameday == len(self.marketdata):
            return "DONE"

    def _get_todays_prices(self, game_day) -> CleanRow:        
        return self.marketdata[game_day]
    
    def _get_todays_decision(self):
        return get_user_input()
    
    def _play_day(self, day_prices: CleanRow) -> bool:
        while True:
            decision = self._get_todays_decision()
            if decision == Action.HOLD:
                return True
            if decision == Action.QUIT:
                print("User quits")
                return False
            success = self.portfolio.handle_transaction(decision, day_prices)
            if success:
                return True
            print("Action not completed. Please choose another.")

    
    def run_game(self):
        while self.gameday < len(self.marketdata):
            print(f"Day: {self.gameday}")
            prices = self._get_todays_prices(self.gameday)
            print(f"Price: {prices.close_price}")

            if not self._play_day(prices):
                return

            print(self.portfolio.get_all_balances())
            self._advance_game_day()

        history_tracker = HistoryTracker(market_data,
                                         market_data_sp,
                                         initial_portfolio_value=start_money, 
                                         portfolio=portfolio)
        report = history_tracker.generate_report()
        print(f"Buy hold gain: {report.buy_hold_gain} vs user gain {report.user_gain} vs SP500 gain {report.stock_gain}")
        

        

game_length = int(3)
start_money = int(100)
clean_data_btc = DataCleaner("data/btc_historical_data.csv").clean_csv()
clean_data_sp = DataCleaner("data/sp500_historical_data.csv").clean_csv()
matched_btc_list, matched_sp_list = match_dates(clean_data_sp, clean_data_btc)

game_setup = GameSetup(matched_btc_list, game_length)
seed = game_setup.seed
market_data = MarketDataLoader(matched_btc_list, seed, game_length).load()
market_data_sp = MarketDataLoader(matched_sp_list, seed, game_length).load()
print(f"Market Data BTC: {market_data}")
print(f"Market Data SP500: {market_data_sp}")
portfolio = Portfolio(start_money)
game_controller = GameController(0, market_data, portfolio)
game_controller.run_game()


