# import pytest
# from portfolio import Action, Portfolio, Currency

# test_portfolio = Portfolio()
# test_portfolio.add(100, Currency.USD)
# decision_handler = DecisionHandler()
# possible_action = decision_handler.handle(100.0, Currency.USD, test_portfolio)


# def test_return_decision_dataclass():
#     assert isinstance(possible_action, Decision)

# def test_return_bool_validity():
#     assert isinstance(possible_action.validity, bool)

# def test_raises_on_nonnumeric_amount():
#     with pytest.raises(ValueError):
#         decision_handler.handle("abc", Currency.USD, test_portfolio)

# def test_raises_on_nonexisting_portfolio():
#     with pytest.raises(ValueError):
#         decision_handler.handle(100.0, Currency.USD, [100, 300, 600])

# def test_returns_true_on_possible_action():
#     possible_action = decision_handler.handle(100.0, Currency.USD, test_portfolio)
#     assert possible_action.validity

# def test_returns_false_on_too_large_amount():
#     impossible_action = decision_handler.handle(99999, Currency.USD, test_portfolio)
#     assert impossible_action.validity == False

# def test_returns_false_on_zero_balance():
#     test_portfolio = Portfolio()
#     impossible_action = decision_handler.handle(1, Currency.USD, test_portfolio)
#     assert impossible_action.validity == False

# def test_returns_false_when_currency_missing_from_portfolio():
#     test_portfolio = Portfolio()
#     decision_handler = DecisionHandler()
#     decision = decision_handler.handle(5.0, Currency.ETH, test_portfolio)
#     assert decision.validity == False