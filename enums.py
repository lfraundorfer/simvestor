from enum import Enum


class Currency(Enum):
    USD = "USD"
    BTC = "BTC"
    ETH = "ETH"


class Action(Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"
    QUIT = "quit"