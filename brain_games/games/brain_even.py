import random
from brain_games.engine import run_game
from brain_games.consts import EVEN_INSTUCTION

def is_even(number):
  return number % 2 == 0


def get_num_and_even_ans() -> tuple:
    number = random.randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'

    return number, answer

