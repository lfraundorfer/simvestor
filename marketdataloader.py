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
        if end_index > len(self.cleandata):
            raise ValueError(f"Game length out of bounds.")
        if self.seed > len(self.cleandata):
            raise ValueError(f"Seed out of bounds.")

        return (start_index, end_index)
    
    def _check_input_validity(self):
        if not isinstance(self.seed, int):
            raise ValueError("Seed must be an integer.")
        if not isinstance(self.gamelength, int):
            raise ValueError("Game length must be an integer.")
        if self.seed < 0:
            raise ValueError("Seed should be positive.")
        if self.gamelength <= 0:
            raise ValueError("Game length should be greater than 0.")

    def load(self) -> list[CleanRow]:
        """
        Returns a slice of cleaned data based on seed and game_length.
        """
        self._check_input_validity()
        start_index, end_index = self._compute_indices()
        try:
            sliced_clean_data = self.cleandata[start_index:end_index]
        except TypeError as e:
            raise TypeError(f"Can not use {e} as seed / gamelength")
        # except IndexError as e:
        #     raise IndexError(f"Game length out of bounds.")
        #this does not raise an error because slicing just automatically stops at the last index
        return sliced_clean_data