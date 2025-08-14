from enums import Action, Currency
from currencyconverter import CurrencyConverter




class Portfolio:
    def __init__(self, start_money:int, balance:dict=None):
        if balance is None:
            self.balance = {currency: 0.0 for currency in Currency}
            self.balance[Currency.USD] = start_money
        else:
            self.balance = balance

    def _validate_input(self, amount: float, currency: Currency) -> float:
        if not isinstance(currency, Currency):
            raise ValueError("Unsupported currency.")
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Cannot use negative amount.")
        return amount
    
    def all_in_amount(self, amount:float, currency:Currency) -> bool:
        return self.balance.get(currency)
    
    def handle_transaction(self, action, daily_price) -> bool:
        if action == Action.HOLD:
            return
        currency_converter = CurrencyConverter()
        if action == Action.BUY:
            source_currency = Currency.USD
            target_currency = Currency.BTC
        elif action == Action.SELL:
            source_currency = Currency.BTC
            target_currency = Currency.USD
        source_balance = self.balance[source_currency]
        if source_balance <=0:
            print(f"No {source_currency.name} to convert!")
            return False
        converted = currency_converter.convert(source_balance, source_currency, target_currency, daily_price)
        self.spend(source_balance, source_currency)
        self.add(converted, target_currency)
        return True
 

    def add(self, amount: float, currency: Currency):
        """Spends supported currency. Raises ValueError on invalid input."""
        amount = self._validate_input(amount, currency)
        self.balance[currency] += amount

    def spend(self, amount, currency:Currency):
        """Sells supported currency. Raises ValueError on invalid input."""
        amount = self._validate_input(amount, currency)
        if self.balance[currency] < amount:
            raise ValueError(f"Not enough {currency.name} to spend.")
        self.balance[currency] -= amount

    def get_all_balances(self):
        return self.balance.copy()



