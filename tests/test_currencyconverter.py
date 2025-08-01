from currencyconverter import CurrencyConverter
from portfolio import Currencies
from datacleaner import DataCleaner
import pytest


dailyprices = {Currencies.BTC : 10, Currencies.ETH: 50}
converter= CurrencyConverter(daily_prices = dailyprices)

def test_returns_float():
    converted = converter.convert(amount=100, source_currency=Currencies.BTC, target_currency=Currencies.ETH)
    assert isinstance(converted, float)

def test_raises_on_nonnumeric_amount():
    with pytest.raises(ValueError):
        converter.convert(amount="100", source_currency=Currencies.BTC, target_currency=Currencies.ETH)
    with pytest.raises(ValueError):
        converter.convert(amount="abc", source_currency=Currencies.BTC, target_currency=Currencies.ETH)

def test_raises_on_identical_source_and_target_currencies():
    with pytest.raises(ValueError):
        converter.convert(amount=100, source_currency=Currencies.BTC, target_currency=Currencies.BTC)
        
def test_input_currency_not_in_prices():
    with pytest.raises(ValueError):
        converter.convert(amount=100, source_currency="TESTCURRENCY", target_currency=Currencies.BTC)
    with pytest.raises(ValueError):
        converter.convert(amount=100, source_currency=Currencies.BTC, target_currency="DOGE")
    with pytest.raises(ValueError):
        converter.convert(amount=100, source_currency="TESTCURRENCY", target_currency="DOGE")


def test_correct_value_calculated():
    dailyprices = {Currencies.BTC : 10, Currencies.ETH: 50}
    converter= CurrencyConverter(daily_prices = dailyprices)
    converted = converter.convert(amount=100, source_currency=Currencies.BTC, target_currency=Currencies.ETH)
    assert converted == 20.0


# def test_raises_on_zero_amount():
#     assert 1
# do not need to raise an error here - it's fine for holding (not buying or selling)

#def test_raise_on_missing_price_info():
#   assert 1
# not needed, datacleaner should provide clean i.e. non empty float data