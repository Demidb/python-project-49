import random
import math

from brain_games.engine import run_game
from brain_games.consts import GCD_INSTUCTION


def get_nums_pair_and_gcd():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    nums_pair = f'{num1} {num2}'
    gcd = math.gcd(num1, num2)

    return nums_pair, str(gcd)

def run_gcd_game():
    run_game(get_nums_pair_and_gcd, GCD_INSTUCTION)



def test_func():  # this is a func for test
    return get_nums_pair_and_gcd()
