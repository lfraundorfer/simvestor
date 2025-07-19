import pytest
from marketdata import MarketData


def test_marketdata_shows_float_value_for_todays_price():
        with pytest.raises(ValueError):
            test_marketdata = MarketData(currentDay = 7)
            float(test_marketdata.btc_price)