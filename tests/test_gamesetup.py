from gamesetup import GameSetup


def test_returns_int_seed():
    test_setup = GameSetup(0,0,0)
    seed = test_setup.generate_seed()
    assert isinstance(seed, int)