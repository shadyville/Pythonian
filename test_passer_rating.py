# import pytest 
from pytest import approx

# import the code to be tested
from passer_rating import nfl_passer_rating

# write a smoke test
def test_smoke():
	assert True == True

# test nfl passer rating Aaron Rodgers example

def test_rodgers_nfl_passer_rating():
	assert nfl_passer_rating(16, 9, 65, 0, 1) == approx(39.8, abs=0.5)
	assert nfl_passer_rating(15, 6, 46, 0, 0) == approx(48.2, abs=0.5)
	assert nfl_passer_rating(28, 20, 218, 1, 0) == approx(106.0, abs=0.5)
	assert nfl_passer_rating(536, 341, 4038, 28, 13) == approx(93.8, abs=0.5)
	assert nfl_passer_rating(541, 350, 4434, 30, 7) == approx(103.2, abs=0.5)



