import pytest
from marketdataloader import MarketDataLoader
from datacleaner import DataCleaner, CleanRow

clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()
market_data = MarketDataLoader(clean_data = clean_data, seed=1, game_length=1).load()


def test_returns_nonempty_list():
    clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()
    market_data = MarketDataLoader(clean_data = clean_data, seed=1, game_length=1).load()
    assert isinstance(market_data, list)
    assert len(market_data) > 0

def test_list_is_correct_length():
    seed = 1
    game_length = 2
    market_data = MarketDataLoader(clean_data, seed, game_length).load()
    assert len(market_data) == int(seed + game_length)

def test_returns_list_of_CleanRow():
    clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()
    market_data = MarketDataLoader(clean_data = clean_data, seed=1, game_length=1).load()
    for daily_data in market_data:
        assert isinstance(daily_data, CleanRow)
