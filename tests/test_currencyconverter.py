from currencyconverter import CurrencyConverter
from portfolio import Currencies
from datacleaner import DataCleaner

def test_returns_float_btc():
    # clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()
    # current_exchange_rate = 100
    # converted_from_usd = CurrencyConverter.convert(amount=100, source_currency=Currencies.USD, target_currency = Currencies.BTC, exchange_rate = current_exchange_rate)
    # converted_from_usd = CurrencyConverter.convert(amount=100, source_currency="USD", target_currency = "BTC", exchange_rate = 2)
    currency_pair_to_convert = CurrencyConverter(amount=100, source_currency="USD", target_currency = "BTC", exchange_rate = 2)
    converted_from_usd = currency_pair_to_convert.convert()
    assert isinstance(converted_from_usd, float)