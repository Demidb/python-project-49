import random

from brain_games.engine import run_game
from brain_games.consts import PRIME_INSTUCTION


def is_prime(num):
  if num < 2:
    return False

  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False

  return True


def get_num_and_prime_ans():
  number = random.randint(1, 100)
  answer = 'yes' if is_prime(number) else 'no'
  return number, answer


def run_prime_game():
  run_game(get_num_and_prime_ans, PRIME_INSTUCTION)


def test_func():  # this is a func for test
  return get_num_and_prime_ans()
