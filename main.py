from gamecontroller import GameController
from user_input_parser import InputParser
from portfolio import Portfolio, Currency
from currencyconverter import CurrencyConverter
from datacleaner import DataCleaner
from gamesetup import GameSetup
from marketdataloader import MarketDataLoader
from decisionhandler import DecisionHandler

# Load and clean data
clean_data = DataCleaner("data/btc_historical_data.csv").clean_csv()

# Setup game (e.g., 100 days simulation)
game_length = 5
seed = GameSetup(clean_data, game_length).generate_seed()
market_data = MarketDataLoader(clean_data, seed, game_length).load()

# Set up other components
portfolio = Portfolio()
portfolio.add(1000, Currency.USD)  # starting funds
converter = CurrencyConverter(daily_prices={Currency.BTC: market_data[0].close_price})
decision_handler = DecisionHandler()
input_parser = InputParser()

# Start the game
game = GameController(market_data, portfolio, converter, decision_handler, input_parser)
game.run_game_loop()
