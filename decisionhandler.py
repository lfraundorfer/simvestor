# from portfolio import Currency, Portfolio, Action

# class DecisionHandler:

#     def _check_input_validity (self, amount, currency_to_check, portfolio: Portfolio):
#         if not isinstance(portfolio, Portfolio):
#             raise ValueError("Invalid portfolio detected.")
#         if not isinstance(currency_to_check, Currency):
#             raise ValueError("Select a valid currency.")
    
#         # move this to input parser!

#     def _define_decision_spend_currency(self, action: Action):
#         # if user sells: we spend the crypto he said
#         if action == Action.sell:
#             return Currency.BTC
#         ## need a dataclass (or something) that connects both the action and the currency, like a transaction object, which also carries validity
#         # this transaction object would then get updated in various functions? idk
#         # if the user buys any crypto, it always defaults to USD
#         # btw - need to check for "sell x usd" -> sell to what?
#         else:
#             return Currency.USD

#     def handle(self, action: Action, currency: Currency, portfolio: Portfolio):
#         self._check_input_validity(currency, portfolio)
#         currency_to_spend = self._define_decision_spend_currency(action)
#             user_input.validity = False
#         else:
#             user_input.validity = True
#         return user_input