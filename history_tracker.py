from dataclasses import dataclass

@dataclass
class HistoryReport:
    buy_hold_gain: float


class HistoryTracker:
    """Records and provides daily snapshots of portfolio balances."""
    def __init__(self, initial_price, final_price, initial_portfolio_value):
        self.initialprice = initial_price
        self.finalprice = final_price
        self.initialportfoliovalue = initial_portfolio_value

    def record(self, day: int, balances: dict):
        # Copy the balances to avoid mutation issues
        self.records.append({"day": day, **balances})

    def get_records(self):
        return self.records
    
    def calc_buy_hold(self):
        btc_bought = self.initialportfoliovalue / self.initialprice
        final_value = btc_bought * self.finalprice
        percent_gain = ((final_value - self.initialportfoliovalue) / self.initialportfoliovalue) * 100
        return percent_gain
    
    def generate_report(self):
        return HistoryReport(buy_hold_gain=self.calc_buy_hold())
    


# buy & hold:
# how much would I have bought (=initial price, to calc it)
# what the price is at the end (=final price)
# all I would need actually: (final_price-initial_price)*[#btc initially bought = start_money / btc_initial]