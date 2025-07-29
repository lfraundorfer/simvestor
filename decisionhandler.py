from dataclasses import dataclass
from portfolio import Action

@dataclass
class Decision:
    validity: bool
    action: str
    amount: float


class DecisionHandler:
    def handle(self, action, amount:float) -> Decision:
        if not isinstance(amount, float):
            raise ValueError("Amount must be numeric.")
        if not isinstance(action, Action):
            raise ValueError("Select a valid action.")
        return Decision(True, action, amount)
    

#rename add / spend to buy / sell in portfolio