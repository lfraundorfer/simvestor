from portfolio import Portfolio, Currencies
import pytest

test_portfolio = Portfolio({Currencies.USD: 10,
                        Currencies.BTC: 0})

def test_spend_more_than_balance():
    with pytest.raises(ValueError):
        test_portfolio.spend(20, Currencies.USD)

def test_spend_negative_amount():
    with pytest.raises(ValueError):
        test_portfolio.spend(-10, Currencies.BTC)

def test_spend_nonexisting_currency():
    with pytest.raises(ValueError):
        test_portfolio.spend(10, "TESTCURRENCY")

def test_spend_nonnumeric_value():
    with pytest.raises(ValueError):
        test_portfolio.spend("one", Currencies.USD)