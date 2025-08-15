from dataclasses import dataclass
from portfolio import Portfolio
from enums import Currency
from datacleaner import CleanRow

@dataclass
class HistoryReport:
    buy_hold_gain: float
    user_gain: float


class HistoryTracker:
    def __init__(self, initial_price:CleanRow, final_price:CleanRow, initial_portfolio_value, portfolio:Portfolio):
        self.initialprice = initial_price
        self.finalprice = final_price
        self.initialportfoliovalue = initial_portfolio_value
        self.portfolio = portfolio
        self.finalportfoliovalue = self._calc_final_portfolio_value()
    
    def calc_buy_hold_performance(self):
        day_one_btc_bought = self.initialportfoliovalue / self.initialprice.close_price
        final_value = day_one_btc_bought * self.finalprice.close_price
        percent_gain = ((final_value - self.initialportfoliovalue) / self.initialportfoliovalue) * 100
        return percent_gain
    
    def _calc_final_portfolio_value(self):
        btc_final_value = self.portfolio.balance[Currency.BTC] * self.finalprice.close_price
        usd_final_value = self.portfolio.balance[Currency.USD]
        return btc_final_value + usd_final_value
    
    def calc_user_performance(self):
        percent_gain = ((self._calc_final_portfolio_value() - self.initialportfoliovalue) / self.initialportfoliovalue)*100
        return percent_gain
    
    def generate_report(self):
        return HistoryReport(buy_hold_gain=self.calc_buy_hold_performance(), user_gain = self.calc_user_performance())
    


# buy & hold:
# how much would I have bought (=initial price, to calc it)
# what the price is at the end (=final price)
# all I would need actually: (final_price-initial_price)*[#btc initially bought = start_money / btc_initial]