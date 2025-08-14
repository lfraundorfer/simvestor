from history_tracker import HistoryTracker, HistoryReport
import pytest

from dataclasses import dataclass

@dataclass
class ExampleValues:
    initial_price: float
    final_price: float
    initial_portfolio_value: float
    expected_percent_gain: float

test_cases = [
    ExampleValues(100, 300, 100, 200.0),   # 200% gain
    ExampleValues(50, 150, 200, 200.0),    # 200% gain
    ExampleValues(200, 100, 150, -50.0),   # -50% loss
]


@pytest.mark.parametrize("test_values", test_cases)
def test_history_tracker_returns_HistoryReport(test_values):
    tracker = HistoryTracker(
        test_values.initial_price,
        test_values.final_price,
        test_values.initial_portfolio_value
    )
    report = tracker.generate_report()
    assert isinstance(report, HistoryReport)


@pytest.mark.parametrize("test_values", test_cases)
def test_calc_buy_hold_returns_float(test_values):
    tracker = HistoryTracker(
        test_values.initial_price,
        test_values.final_price,
        test_values.initial_portfolio_value
    )
    gains = tracker.calc_buy_hold()
    assert isinstance(gains, float)

@pytest.mark.parametrize("test_values", test_cases)
def test_calc_buy_hold_is_correct(test_values):
    tracker = HistoryTracker(
        test_values.initial_price,
        test_values.final_price,
        test_values.initial_portfolio_value
    )
    report = tracker.generate_report()
    assert pytest.approx(report.buy_hold_gain, abs=1e-2) == test_values.expected_percent_gain



