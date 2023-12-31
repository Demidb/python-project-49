import prompt
import random
from math import gcd


def main():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'Find the greatest common divisor of given numbers.')
    count = 0
    for n in range(3):
        number = random.randint(1, 100)
        number1 = random.randint(1, 100)
        print(f'Question: {number} {number1}')
        answer = prompt.string('Your answer: ')
        true_answer = gcd(number, number1)
        if answer == str(true_answer):
            print('Correct!')
            count += 1
        else:
            print(f" {answer} is wrong answer ;(. "
                  f"Correct answer was {true_answer}."
                  f"\nLet's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
