import pytest
from gamecontroller import GameController
from datacleaner import CleanRow
import datetime

@pytest.fixture
def test_market_data():
    return [CleanRow(date=datetime.date(2015, 2, 4), close_price=227.129), 
            CleanRow(date=datetime.date(2015, 2, 5), close_price=226.147), 
            CleanRow(date=datetime.date(2015, 2, 6), close_price=216.969), 
            CleanRow(date=datetime.date(2015, 2, 7), close_price=222.236)]

def test_advances_day(test_market_data):
    game_day = 15
    game_controller = GameController(game_day, test_market_data)
    game_controller._advance_game_day()
    assert game_controller.gameday == game_day + 1

def test_returns_dict(test_market_data):
    game_day = 1
    game_controller = GameController(game_day, test_market_data)
    daily_price_dict = game_controller._get_todays_prices(game_day)
    assert isinstance(daily_price_dict, CleanRow)

def test_get_todays_decision(monkeypatch, test_market_data):
    game_controller = GameController(1, test_market_data, portfolio=None)

    # Pretend the user typed "buy"
    monkeypatch.setattr("user_input_parser.input", lambda _: "buy")

    decision = game_controller._get_todays_decision()
    assert decision == Action.BUY