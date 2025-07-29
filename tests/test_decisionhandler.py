import pytest
from decisionhandler import DecisionHandler, Decision
from portfolio import Action


decision_handler = DecisionHandler()
decision = decision_handler.handle(Action.add, 100.0)

def test_return_decision_dataclass():
    assert isinstance(decision, Decision)

def test_return_correct_action():
    decision = decision_handler.handle(Action.add, 100.0)
    assert decision.action == Action.add

def test_return_bool_validity():
    assert isinstance(decision.validity, bool)

def test_invalid_amount():
    with pytest.raises(ValueError):
        decision_handler.handle(Action.add, "abc")


def test_invalid_action():
    with pytest.raises(ValueError):
        decision_handler.handle("test_action", 100.0)

#def test_valid_action


#def test_invalid_action


#will I also involve the currency here? or does currencyconv check this?



#amount = self._validate_input(amount, currency, "spend")
#in portfolio.py
# so I return a spend / add decision
# in gamecontroller, make user set an amount that will return a valid spend/add