# Receives a random seed (integer) and a timeinterval(int), returns a list of (seed+timeinterval) closing prices (floats)

from datacleaner import CleanRow

class MarketDataLoader:
    def __init__(self, clean_data: list, seed:int, game_length:int):
        self.cleandata = clean_data
        self.seed = seed
        self.gamelength = game_length

    def _compute_indices(self):
        start_index = self.seed
        end_index = start_index + self.gamelength +1 #slicing excludes the last index, hence the +1

        return (start_index, end_index)
    

    def load(self) -> list[CleanRow]:
        """
        Returns a slice of cleaned data based on seed and game_length.
        """
        start_index, end_index = self._compute_indices()
        try:
            sliced_clean_data = self.cleandata[start_index:end_index]
        except TypeError as e:
            raise TypeError(f"Can not use as seed / gamelength: {e}")
        # except IndexError as e:
        #     raise IndexError(f"Game length out of bounds.")
        #this does not raise an error because slicing just automatically stops at the last index
        return sliced_clean_data