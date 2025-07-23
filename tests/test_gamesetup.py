from gamesetup import GameSetup
from datacleaner import DataCleaner
import pytest
    

clean_data = DataCleaner("tests/test_csv_files/btc_test_data.csv").clean_csv()


def test_returns_int_seed():
    game_length = 3
    test_setup = GameSetup(clean_data,game_length)
    seed = test_setup.generate_seed()
    assert isinstance(seed, int)

def test_seed_within_bounds():
    
    game_length = 3
    test_setup = GameSetup(clean_data,game_length)
    seed = test_setup.generate_seed()
    assert seed < len(clean_data) - game_length


def test_raise_on_nonnumeric_game_length():
    with pytest.raises(ValueError):
        seed = 1
        game_length = "one"
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)


def test_raise_on_nonnumeric_seed():
    with pytest.raises(ValueError):
        seed = "two"
        game_length = 1
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)


def test_raise_on_negative_game_length():
    with pytest.raises(ValueError):
        seed = 1
        game_length = "one"
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)


def test_raise_on_negative_seed():
    with pytest.raises(ValueError):
        seed = "two"
        game_length = 1
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)

def test_raise_on_float_seed():
    with pytest.raises(ValueError):
        seed = 1.0
        game_length = 1
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)


def test_raise_on_float_game_length():
    with pytest.raises(ValueError):
        seed = 1
        game_length = 1.0
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)


def test_raise_on_game_length_out_of_bounds():
    with pytest.raises(ValueError):
        seed = 1
        game_length = 999999
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)

def test_raise_on_seed_out_of_bounds():
    with pytest.raises(ValueError):
        seed = 9999999
        game_length = 1
        GameSetup(clean_data,game_length)._check_input_validity(seed, game_length)