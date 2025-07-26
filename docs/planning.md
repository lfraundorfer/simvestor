# User Story

The user presses start and is assigned a random historic 100 day period of the BTC price graph, as well as 100 USD.

Then, the user can "play" the period: Each day, they are asked to buy, hold, or sell. Based on the graph and price info they see.

Their profit is calculated, with them having the new sum available each day.

In the background, 100 USD are invested on day 1 (to simulate a buy & hold strategy).

In addition, 1 USD is invested every day (to simulate a DCA strategy).

At the end of the 100 days, the comparison is made (and visualized) to see which strategy won.

# Assumptions

No fees, no taxes, one trade per day

# Classes & Objects

-The user loads a historic dataset
-Object: MarketDataLoader
-Method: load_historical_prices()
-Responsibility:
-Loads data from csv
-Returns a list of CleanRow (price + date) per day, for a time interval I specify in GameSetup, starting at a random seed (as per GameSetup)

-The user decides on buy | hold | sell
-Object: GameController
-Responsibility:
-advance_game: gets the user's decision from the UI and sends it to currencyConverter (new balances -> portfolio) and advances the gameDay (new value from marketdata list)

-Object: GameSetup
-Method: setup_gamelength()
-Default to 10, lets the user enter a gamelength (int), which is then passed to MarketDataLoader
-Method: generate_seed()
-Generates a random, yet valid seed (int)
-Validity meaning seed + gamelength do not exceed the available data set
-Calls MarketDataLoader with the seed + game length to get a random slice of the daily price data

-Object: DecisionHandler
-Responsibility: reads Portfolio to see the balances, checks validity of operation, and then sends a valid decision to GameController

-Object: Portfolio
-Method: spend(), add()
-with new balance (USD and/or BTC)

-Object: CurrencyConverter
-Responsibility: receives a float value of BTC / USD and converts, while rounding to a manageable level
-Method: convert_currency()
-To calculate the correct values to be sent to the portfolio
-Method: round_values()
-I guess this doesn't have to be a method, can just auto-round

-Object:GameConfig
-Contains the interval for the timeframe, the mode for the DataLoader, the
currencies, etc
-Will be passed around to whichever module needs it, will make sure the data values are valid

-Object:DataCleaner
-cleans the file and passes btc_price(float), and date(datetime) on to MarketDataLoader, who then checks only if a valid response has been loaded, so this is its sole responsibility. the cleaner has the only responsibility of CLEANING the data, so I don't muddy the waters

# Next Steps:

-Figure out the Portfolio object
-Tests:
-Scenario: User wants to spend more than they have
-Input: 120 USD at 100 USD balance
-Expected Result: error message, user is prompted to try again
-Scenario: User wants to spend a negative value
-Input: -120 USD
-Expected Result: error message, user is prompted to try again
-Scenario: User wants to spend a non-numeric value
-Input: ABCD
-Expected Result: error message, user is prompted to try again
