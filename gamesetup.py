import random

class GameSetup():
    def __init__(self, market_data, seed=0, game_length=1):
        self.seed = seed
        self.gamelength = game_length
        self.marketdata = market_data

    def _check_seed_validity(self):
        return 1
    #is int, positive
    
    def _check_game_length_validity(self):
        return 1
    #is int, positive

    def _define_seed_bounds(self):
        maximum_seed_value = len(self.gamelength)
        return maximum_seed_value
    
    def generate_seed(self):
        # maximum_seed_value = self._define_seed_bounds()
        seed = random.randint(0, 100)
        print(seed)
        return seed

test_setup = GameSetup(0,0,0)
test_seed = test_setup.generate_seed()
    #get game_length
    #then generate seed according to the possible bounds

    #move the check of maximum game_length to this, away from marketdataloader; that should already receive valid seed + game_length