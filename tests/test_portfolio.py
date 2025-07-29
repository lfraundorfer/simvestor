from portfolio import Portfolio, Currency
import pytest

test_portfolio = Portfolio({Currency.USD: 10,
                        Currency.BTC: 0})

# Tests for 'spend' method
def test_spend_more_than_balance():
    with pytest.raises(ValueError):
        test_portfolio.spend(20, Currency.USD)

def test_spend_negative_amount():
    with pytest.raises(ValueError):
        test_portfolio.spend(-10, Currency.BTC)

def test_spend_nonexisting_currency():
    with pytest.raises(ValueError):
        test_portfolio.spend(10, "TESTCURRENCY")

def test_spend_nonnumeric_value():
    with pytest.raises(ValueError):
        test_portfolio.spend("one", Currency.USD)

# Tests for 'add' method

def test_add_negative_amount():
    with pytest.raises(ValueError):
        test_portfolio.add(-10, Currency.BTC)

def test_add_nonexisting_currency():
    with pytest.raises(ValueError):
        test_portfolio.add(10, "TESTCURRENCY")

def test_add_nonnumeric_value():
    with pytest.raises(ValueError):
        test_portfolio.add("one", Currency.USD)


# Tests for 'get_all_balances' method

def test_return_copy_of_balance():
    test_balance = test_portfolio.get_all_balances()
    test_balance[Currency.USD] += 1
    assert test_portfolio.balance[Currency.USD] == 10
