from dataclasses import dataclass
from portfolio import Action, Currency, Portfolio

@dataclass
class Decision:
    validity: bool
    amount: float
    currency_to_spend: Currency


class DecisionHandler:
    def handle(self, amount, currency_to_spend:Currency, portfolio: Portfolio) -> Decision:
        if not isinstance(portfolio, Portfolio):
            raise ValueError("Invalid portfolio detected.")
        if not isinstance(amount, (float,int)):
            raise ValueError("Amount must be numeric.")
        if not isinstance(currency_to_spend, Currency):
            raise ValueError("Select a valid currency.")
        if not portfolio.can_spend(amount, currency_to_spend): 
            return Decision(False, amount, currency_to_spend)
        return Decision(True, amount, currency_to_spend)
    