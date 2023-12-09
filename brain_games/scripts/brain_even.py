import prompt
import random


def is_even(number):
    return number % 2 == 0


def main():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        expected_answer = 'yes' if is_even(number) else 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer == expected_answer:
            print('Correct!')
            count += 1
        else:
            correct_answer = 'yes' if is_even(number) else 'no'
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f"\nLet's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
