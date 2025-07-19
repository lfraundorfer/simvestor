from enum import Enum

class Currencies(Enum):
    USD = "USD"
    BTC = "BTC"

class Portfolio:
    def __init__(self, balance=None):
        if balance is None:
            self.balance = {currency: 0.0 for currency in Currencies}
        else:
            self.balance = balance


    def spend(self, spending_amount, spending_currency):
        try:
            float(spending_amount)
        except ValueError:
            raise ValueError("Spending amount must be a number.")
        if spending_amount < 0:
            raise ValueError("Cannot spend negative amount.")
        if spending_currency not in Currencies:
            raise ValueError("Cannot spend unavailable currency.")
        available_balance = self.balance[spending_currency] 
        if available_balance < spending_amount:
            raise ValueError("Cannot spend more than available balance.")
        self.balance[spending_currency] -= spending_amount


port1 = Portfolio({Currencies.USD: 100,
                        Currencies.BTC: 0})
