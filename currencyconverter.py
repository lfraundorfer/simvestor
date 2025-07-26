
class CurrencyConverter:

    def __init__(self, amount, source_currency, target_currency, exchange_rate):
        self.amount = amount
        self.sourcecurrency = source_currency
        self.targetcurrency = target_currency
        self.exchangerate = exchange_rate


    def convert(self):
        converted_currency = self.amount / self.exchangerate
        converted_currency_float = float(converted_currency)
        return float(converted_currency_float)