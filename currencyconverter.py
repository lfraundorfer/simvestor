from portfolio import Currencies


class CurrencyConverter:

    def __init__(self, daily_prices: dict):
        self.dailyprices = daily_prices

    def _calc_usd_rate(self, currency_for_usd_rate) ->float:
        if currency_for_usd_rate != Currencies.USD:
            source_usd_rate = 1 / self.dailyprices[currency_for_usd_rate]
            return source_usd_rate        
        return 1.0

    def convert(self, amount, source_currency, target_currency) -> float:
        if not isinstance(amount, (int, float)):
            raise ValueError("Please specify a numeric value to convert.")
        if source_currency not in self.dailyprices:
            raise ValueError(f"Source currency '{source_currency}' not found.")
        if target_currency not in self.dailyprices:
            raise ValueError(f"Target currency '{target_currency}' not found.")
        if source_currency == target_currency:
            raise ValueError("Please specify two different currencies to convert.")
        source_currency_usd_rate = self._calc_usd_rate(source_currency)
        target_currency_usd_rate = self._calc_usd_rate(target_currency)
        exchange_rate = source_currency_usd_rate/target_currency_usd_rate
        converted_amount = amount / exchange_rate
        # converted_currency_float = float(converted_currency)
        print(f"Converting {amount} of {source_currency} to {target_currency} at an exchange rate of {exchange_rate} resulting in {converted_amount}")
        return converted_amount
    
