import random
from datacleaner import CleanRow, DataCleaner

class GameSetup():
    def __init__(self, clean_data:list[CleanRow], game_length:int=1):
        self.cleandata = clean_data
        self.gamelength = game_length

    
    def _check_input_validity(self, seed, gamelength):
        if not isinstance(seed, int):
            raise ValueError("Seed must be an integer.")
        if not isinstance(gamelength, int):
            raise ValueError("Game length must be an integer.")
        if seed < 0:
            raise ValueError("Seed should be positive.")
        if gamelength <= 0:
            raise ValueError("Game length should be greater than 0.")
        if seed + gamelength + 1 > len(self.cleandata):
            raise ValueError(f"Game length out of bounds.")
        if seed > len(self.cleandata):
            raise ValueError(f"Seed out of bounds.")


    def _get_clean_data(self) -> list[CleanRow]:
        return []

    def _define_seed_bounds(self) -> int:
        maximum_seed_value = len(self.cleandata) - self.gamelength -1
        return maximum_seed_value
    
    def generate_seed(self) -> int:
        maximum_seed_value = self._define_seed_bounds()
        seed = random.randint(0, maximum_seed_value)
        self._check_input_validity(seed, self.gamelength)
        print(seed)
        return seed


    #get game_length
    #then generate seed according to the possible bounds

    #move the check of maximum game_length to this, away from marketdataloader; that should already receive valid seed + game_length