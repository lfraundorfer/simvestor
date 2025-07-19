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
-Object: MarketData
-Method: load_from_csv()
-Responsibility:
-should know the current day & price, and provide (n-1) and (n) values at any given time, so we can calculate profit
-Should also know when the user has made a decision

-The user decides on buy | hold | sell
-Object: Gamestate
-Method: calculate_return()

-Object: Portfolio
-Method: update_balance()
-with new balance (USD and/or BTC)

-Object: CurrencyMath
-Method: check_assets()
-can I even perform the desired action? (enough assets?)
-Method: round_values()

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
