import pytest
from marketdataloader import MarketDataLoader
from datacleaner import DataCleaner


def test_returns_list():
    clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()
    market_data = MarketDataLoader(clean_data = clean_data, seed=1, time_interval=1).load()
    assert isinstance(market_data, list)
