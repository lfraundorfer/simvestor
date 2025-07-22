# Receives a random seed (integer) and a timeinterval(int), returns a list of (seed+timeinterval) closing prices (floats)

class MarketDataLoader:
    def __init__(self, clean_data: list, seed:int, time_interval:int):
        self.cleandata = clean_data
        self.seed = seed
        self.timeinterval = time_interval

    def load(self):

        return self.cleandata