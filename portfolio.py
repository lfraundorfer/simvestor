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

    def _validate_input(self, amount, currency, action):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError(f"{action} amount must be a number.")
        if amount < 0:
            raise ValueError(f"Cannot {action} negative amount.")
        if currency not in Currencies:
            raise ValueError(f"Cannot {action} unavailable currency.")
        return amount
        

    def spend(self, amount, currency):
        """Spends a given amount of supported currency. Raises ValueError on invalid input."""
        amount = self._validate_input(amount, currency, "spend")
        available_balance = self.balance[currency] 
        if available_balance < amount:
            raise ValueError("Cannot spend more than available balance.")
        self.balance[currency] -= amount

    def add(self, amount, currency):
        """Adds a given amount of supported currency. Raises ValueError on invalid input."""
        amount = self._validate_input(amount, currency, "add")
        self.balance[currency] += amount

    def get_all_balances(self):
        return self.balance.copy()



