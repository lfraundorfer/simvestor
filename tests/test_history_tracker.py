from history_tracker import HistoryTracker, HistoryReport
from portfolio import Portfolio
import pytest
from enums import Currency

from dataclasses import dataclass

@pytest.fixture
def default_portfolio():
    return Portfolio(100, {Currency.USD: 0, Currency.BTC: 0})

@dataclass
class ExampleValues:
    initial_price: float
    final_price: float
    initial_portfolio_value: float
    expected_buy_hold_percent_gain: float

test_cases = [
    ExampleValues(100, 300, 100, 200.0),   # 200% gain
    ExampleValues(50, 150, 200, 200.0),    # 200% gain
    ExampleValues(200, 100, 150, -50.0),   # -50% loss
]

@dataclass
class PortfolioTestCase:
    values: ExampleValues
    user_portfolio_balances: dict  # like {Currency.USD: 100, Currency.BTC: 2}
    expected_user_percent_gain: float

portfolio_test_cases = [
PortfolioTestCase(
    values=ExampleValues(100, 300, 100, 200.0),
    user_portfolio_balances={Currency.USD: 100, Currency.BTC: 2},
    expected_user_percent_gain=600.0
),
PortfolioTestCase(
    values=ExampleValues(100, 300, 100, 200.0),
    user_portfolio_balances={Currency.USD: 100, Currency.BTC: 0},
    expected_user_percent_gain=0.0
),
PortfolioTestCase(
    values=ExampleValues(100, 150, 100, 50.0),
    user_portfolio_balances={Currency.USD: 0, Currency.BTC: 1},
    expected_user_percent_gain=50.0
)
]



@pytest.mark.parametrize("test_values", test_cases)
def test_history_tracker_returns_HistoryReport(test_values, default_portfolio):
    tracker = HistoryTracker(
        test_values.initial_price,
        test_values.final_price,
        test_values.initial_portfolio_value,
        default_portfolio
    )
    report = tracker.generate_report()
    assert isinstance(report, HistoryReport)


@pytest.mark.parametrize("test_values", test_cases)
def test_calc_buy_hold_returns_float(test_values, default_portfolio):
    tracker = HistoryTracker(
        test_values.initial_price,
        test_values.final_price,
        test_values.initial_portfolio_value,
        default_portfolio
    )
    buy_hold_gain = tracker.calc_buy_hold_performance()
    assert isinstance(buy_hold_gain, float)

@pytest.mark.parametrize("test_values", test_cases)
def test_calc_buy_hold_is_correct(test_values, default_portfolio):
    tracker = HistoryTracker(
        test_values.initial_price,
        test_values.final_price,
        test_values.initial_portfolio_value,
        default_portfolio
    )
    report = tracker.generate_report()
    assert pytest.approx(report.buy_hold_gain, abs=1e-2) == test_values.expected_buy_hold_percent_gain


@pytest.mark.parametrize("test_portfolios", portfolio_test_cases)
def test_user_gain_from_portfolio(test_portfolios):
    portfolio = Portfolio(100, test_portfolios.user_portfolio_balances)
    tracker = HistoryTracker(
        test_portfolios.values.initial_price,
        test_portfolios.values.final_price,
        test_portfolios.values.initial_portfolio_value,
        portfolio
    )
    report = tracker.generate_report()
    assert pytest.approx(report.user_gain, abs=1e-2) == test_portfolios.expected_user_percent_gain
