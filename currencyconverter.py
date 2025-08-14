from enums import Currency
from datacleaner import CleanRow


class CurrencyConverter:

    def _calc_usd_rate(self, currency_for_usd_rate, dailyprice:CleanRow) ->float:
        if currency_for_usd_rate != Currency.USD:
            source_usd_rate = 1 / dailyprice.close_price
            return float(source_usd_rate)        
        return 1.0
    
    def _validate_input(self, amount, source_currency, target_currency):
        if not isinstance(amount, (int, float)):
            raise ValueError("Please specify a numeric value to convert.")
        if source_currency == target_currency:
            raise ValueError("Please specify two different currencies to convert.")

    def convert(self, amount, source_currency: Currency, target_currency:Currency, daily_price:CleanRow) -> float:
        self._validate_input(amount, source_currency, target_currency)
        if source_currency == Currency.USD and target_currency == Currency.BTC:
            return amount / daily_price.close_price

        elif source_currency == Currency.BTC and target_currency == Currency.USD:
            return amount * daily_price.close_price

        else:
            raise NotImplementedError("Only USD <-> BTC conversion is supported for now.")
