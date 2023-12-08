import random

def main():
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    count = 0
    name = input('Welcome to the Brain Games!\n'
                 'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'Answer "yes" if given number is prime. Otherwise answer "no"')
    for n in range(3):
            number = random.randint(2, 50)
            user_answer = input(f"Is {number} a prime number? (yes/no): ").lower()
            
            if user_answer in ('yes', 'no'):
                correct_answer = 'yes' if is_prime(number) else 'no'

                if user_answer == correct_answer:
                    print("Correct!")
                    count +=1
    if count == 3:
        print("Congratulations!")
    else:
        print(f"Sorry, {name}.{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {name}")

main()