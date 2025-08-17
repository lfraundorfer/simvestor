import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from enums import Action

prices = [100, 110, 67, 223]  # Example data

class DataPlotter():
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
    
    def draw(self, prices):
        actions = []
        for day in range(1, len(prices)):
            # clears subplot so the new one does not overlap
            self.ax.clear()
            # plot until current day, with o marker
            self.ax.plot(prices[:day+1], marker='o')
            self.ax.set_title(f"Day {day}")
            #day starts at 1, and I need ticks to go to day +1 
            ticks = list(range(1, day + 2))
            labels = [f"Day {i}" for i in ticks]
            self.ax.set_xticks(ticks)
            self.ax.set_xticklabels(labels)

            for i, action in enumerate(actions, start=1):
                price = prices[i]
                color = {Action.BUY: "green", Action.SELL: "red", Action.HOLD: "gray"}.get(action, "black")
                marker = {Action.BUY: "^", Action.SELL: "v", Action.HOLD: "o"}.get(action, "o")
                self.ax.plot(i, price, marker=marker, color=color, markersize=10, linestyle="None")

            # pause execution briefly to allow the GUI to update the plot
            plt.pause(0.1)

            choice = Action[input("Buy, Hold, Sell, or Quit? ").strip().upper()]
            if choice == Action.QUIT:
                break
            actions.append(choice)

        plt.ioff()
        plt.show()


data_plotter = DataPlotter()
data_plotter.draw(prices)


# def draw_plot(prices):
#     #interactive mode: or plt.show() pauses execution until the plot window is closed
#     plt.ion()
#     #fig: entire canvas. ax = single subplot
#     fig, ax = plt.subplots()
#     # ax.plot creates a line object, to be updated later
#     # and "line," unpacks the first (in this case, only) "Line2D" object of the ax.plot tuple
#     line, = ax.plot([], [])

#     actions = []

#     for day in range(1, len(prices)):
#         # clears subplot so the new one does not overlap
#         ax.clear()
#         # plot until current day, with o marker
#         ax.plot(prices[:day+1], marker='o')
#         ax.set_title(f"Day {day}")
#         #day starts at 1, and I need ticks to go to day +1 
#         ticks = list(range(1, day + 2))
#         labels = [f"Day {i}" for i in ticks]
#         ax.set_xticks(ticks)
#         ax.set_xticklabels(labels)
#         # pause execution briefly to allow the GUI to update the plot

#         for i, action in enumerate(actions, start=1):
#             price = prices[i]
#             color = {"buy": "green", "sell": "red", "hold": "gray"}.get(action, "black")
#             marker = {"buy": "^", "sell": "v", "hold": "o"}.get(action, "o")
#             ax.plot(i, price, marker=marker, color=color, markersize=10, linestyle="None")
#         plt.pause(0.1)

#         choice = input("Buy, Hold, Sell, or Quit? ").strip().lower()
#         if choice == "quit":
#             break
#         actions.append(choice)

#     plt.ioff()
#     plt.show()
