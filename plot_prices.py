import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from enums import Action
import numpy as np

class DataPlotter():
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.colormap = {Action.BUY: "green",
                          Action.SELL: "red", 
                          Action.HOLD: "gray"}
        self.markermap = {Action.BUY: "^", 
                          Action.SELL: "v", 
                          Action.HOLD: "o"}
    
    def draw(self, prices:list[float], history_of_actions: list[Action]):
        for day in range(len(prices)):
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

            if history_of_actions:
                for i, action in enumerate(history_of_actions, start=1):
                    price = prices[i]
                    color = self.colormap.get(action, "black")
                    marker = self.markermap.get(action, "o")
                    self.ax.plot(i, price, marker=marker, color=color, markersize=10, linestyle="None")

            # pause execution briefly to allow the GUI to update the plot
            plt.pause(0.1)

            if history_of_actions and history_of_actions[-1] == Action.QUIT:
                break

    def finalize_plot(self):
        plt.ioff()
        plt.show()


