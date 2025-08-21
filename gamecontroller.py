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
from plot_prices import DataPlotter



class GameController():
    def __init__(self, game_day:int, market_data: list, portfolio: Portfolio):
        self.gameday = game_day or 1
        self.marketdata = market_data
        self.portfolio = portfolio
        self.history_of_actions = []

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
            self.history_of_actions.append(decision)
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
        list_of_prices_until_current_day = [self.marketdata[0].close_price]
        while self.gameday < len(self.marketdata):
            print(f"Day: {self.gameday}")
            today_price = self._get_todays_prices(self.gameday)
            print(f"Price: {today_price.close_price}")
            list_of_prices_until_current_day.append(today_price.close_price)

            data_plotter.draw(list_of_prices_until_current_day, self.history_of_actions)

            if not self._play_day(today_price):
                return

            print(self.portfolio.get_all_balances())
            self._advance_game_day()

        history_tracker = HistoryTracker(market_data_btc,
                                         market_data_sp,
                                         initial_portfolio_value=start_money, 
                                         portfolio=portfolio,
                                         last_btc_data_entry=last_btc_data,
                                         last_sp_data_entry = last_sp_data)
        report = history_tracker.generate_report()
        print(f"Buy hold gain: {report.buy_hold_gain} vs user gain {report.user_gain} vs SP500 gain {report.stock_gain} vs bogle BTC gain {report.bogle_btc_gain} vs bogle SP500 gain {report.bogle_stock_gain}")
        data_plotter.finalize_plot()


        

        

game_length = int(5)
start_money = int(100)
data_cleaner = DataCleaner()
clean_data_btc = data_cleaner.clean_csv("data/btc_historical_data.csv")
clean_data_sp = data_cleaner.clean_csv("data/sp500_historical_data.csv")
matched_btc_list, matched_sp_list = match_dates(clean_data_sp, clean_data_btc)

game_setup = GameSetup(matched_btc_list, game_length, step_size=30)
seed = game_setup.seed
market_data_loader = MarketDataLoader(seed, game_length, step_size = 30)
market_data_btc = market_data_loader.load(matched_btc_list)
market_data_sp = market_data_loader.load(matched_sp_list)

last_btc_data = market_data_loader.load_last_day(matched_btc_list)
last_sp_data = market_data_loader.load_last_day(matched_sp_list)

# print(last_btc_data, last_sp_data)

print(f"Market Data BTC: {market_data_btc}")
print(f"Market Data SP500: {market_data_sp}")
portfolio = Portfolio(start_money)
game_controller = GameController(0, market_data_btc, portfolio)
data_plotter = DataPlotter()
game_controller.run_game()



