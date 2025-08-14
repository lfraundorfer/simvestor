from enums import Action


def get_user_input() -> Action:
    while True:
        user_input = input("Please enter today's decision [buy/hold/sell], or 'quit': ").strip().upper()
        try:
            return Action[user_input]
        except KeyError:
            print("Invalid action or currency. Please use buy/hold/sell and USD/BTC.")

