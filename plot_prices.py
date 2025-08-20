import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from enums import Action
import numpy as np

class DataPlotter():
    def __init__(self):
        plt.ion()
        self.colormap = {Action.BUY: "green",
                          Action.SELL: "red", 
                          Action.HOLD: "gray"}
        self.markermap = {Action.BUY: "^", 
                          Action.SELL: "v", 
                          Action.HOLD: "o"}
    
    def draw(self, prices:list[float], history_of_actions: list[Action]):
        if not hasattr(self, 'ax'):
            self.fig, self.ax = plt.subplots()
        # clears subplot so the new one does not overlap
        self.ax.clear()
        self.ax.grid(True)
        x = np.arange(1, len(prices) +1)
        y = prices
        # plot until current day, with o marker
        self.ax.plot(x,y, marker='o')
        self.ax.set_title(f"Day {len(prices) -1}")
        #day starts at 1, and I need ticks to go to day +1 
        ticks = x
        labels = [f"Day {i}" for i in ticks]
        self.ax.set_xticks(ticks)
        self.ax.set_xticklabels(labels)

        for i, action in enumerate(history_of_actions):
            x = i + 2  # +1 to shift from 0-based index, +1 because prices includes one more than actions
            if x <= len(prices):
                price = prices[x - 1]
                color = self.colormap.get(action, "black")
                marker = self.markermap.get(action, "o")
                self.ax.plot(x, price, marker=marker, color=color, markersize=10, linestyle="None")

        # pause execution briefly to allow the GUI to update the plot
        plt.pause(0.1)



    def finalize_plot(self):
        plt.ioff()
        plt.show()


