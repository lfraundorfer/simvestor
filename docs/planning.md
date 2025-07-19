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
-Loads data from csv or API
-Returns a list of prices per day
-Can be expanded to a dict if I want to add more currencies later

-The user decides on buy | hold | sell
-Object: GameController
-Responsibility:
-advance_game: gets the user's decision from the UI and sends it to currencyConverter (new balances -> portfolio) and advances the gameDay (new value from marketdata list)

-Object: GameSetup
-Calls MarketDataLoader with the given interval amount, picking a random interval

-Object: DecisionHandler
-Responsibility: reads Portfolio to see the balances, checks validity of operation, and then sends a valid decision to GameController

-Object: Portfolio
-Method: spend(), add()
-with new balance (USD and/or BTC)

-Object: CurrencyConverter
-Method: convert_currency()
-To calculate the correct values to be sent to the portfolio
-Method: round_values()
-I guess this doesn't have to be a method, can just auto-round

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
