import random


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    count = 0
    name = input('Welcome to the Brain Games!\n'
                 'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = random.randint(2, 50)
        print(f'Question: {number}')
        user_answer = input('Your answer: ').lower()
        if user_answer in ('yes', 'no'):
            correct_answer = 'yes' if is_prime(number) else 'no'
            if user_answer == correct_answer:
                print("Correct!")
                count += 1
            else:
                print(f"{user_answer} is wrong answer ;(. "
                      f"Correct answer was {correct_answer}."
                      f"\nLet's try again, {name}!")
                break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
