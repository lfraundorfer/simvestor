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

def test_raise_on_nonnumeric_game_length():
    with pytest.raises(ValueError):
        seed = 1
        game_length = "one"
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_nonnumeric_seed():
    with pytest.raises(ValueError):
        seed = "two"
        game_length = 1
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_negative_game_length():
    with pytest.raises(ValueError):
        seed = 1
        game_length = "one"
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_negative_seed():
    with pytest.raises(ValueError):
        seed = "two"
        game_length = 1
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_float_seed():
    with pytest.raises(ValueError):
        seed = 1.0
        game_length = 1
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_float_game_length():
    with pytest.raises(ValueError):
        seed = 1
        game_length = 1.0
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_game_length_out_of_bounds():
    with pytest.raises(ValueError):
        seed = 1
        game_length = 999999
        MarketDataLoader(clean_data, seed, game_length).load()

def test_raise_on_seed_out_of_bounds():
    with pytest.raises(ValueError):
        seed = 9999999
        game_length = 1
        MarketDataLoader(clean_data, seed, game_length).load()

def test_returns_list_of_CleanRow():
    clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()
    market_data = MarketDataLoader(clean_data = clean_data, seed=1, game_length=1).load()
    for daily_data in market_data:
        assert isinstance(daily_data, CleanRow)
