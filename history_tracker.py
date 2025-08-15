from dataclasses import dataclass
from portfolio import Portfolio
from enums import Currency
from datacleaner import CleanRow

@dataclass
class HistoryReport:
    buy_hold_gain: float
    user_gain: float


class HistoryTracker:
    def __init__(self, market_data:list[CleanRow], initial_portfolio_value:float, portfolio:Portfolio):
        self.marketdata = market_data
        self.initialportfoliovalue = initial_portfolio_value
        self.portfolio = portfolio
        self.finalportfoliovalue = self._calc_final_portfolio_value()
    
    def calc_buy_hold_performance(self):
        percent_gain = ((self.marketdata[-1].close_price / self.marketdata[1].close_price) -1 ) * 100
        return round(percent_gain,2)
    
    def _calc_final_portfolio_value(self):
        btc_final_value = self.portfolio.balance[Currency.BTC] * self.marketdata[-1].close_price
        usd_final_value = self.portfolio.balance[Currency.USD]
        return btc_final_value + usd_final_value
    
    def calc_user_performance(self):
        percent_gain = ((self._calc_final_portfolio_value() - self.initialportfoliovalue) / self.initialportfoliovalue)*100
        return round(percent_gain,2)
    
    def calc_sp500_performance(self):
        return 
    
    def generate_report(self):
        return HistoryReport(buy_hold_gain=self.calc_buy_hold_performance(), user_gain = self.calc_user_performance())
    


# buy & hold:
# how much would I have bought (=initial price, to calc it)
# what the price is at the end (=final price)
# all I would need actually: (final_price-initial_price)*[#btc initially bought = start_money / btc_initial]