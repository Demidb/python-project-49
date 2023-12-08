import prompt
import random
def main():
    
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'What is the result of the expression?')
    count = 0
    for n in range(3):
        number = random.randint(1, 100)
        number1 = random.randint(1, 100)
        operand = random.choice(["+", "-", "*"])
        print(f'Question: {number} {operand} {number1}')
        if operand == "+":
            sum = number + number1
            answer = prompt.string('Your answer: ')
            if answer == str(sum):
                print('Correct!')
                count = count + 1
            else:
                print(f' {answer} is wrong answer ;(. Correct answer was {sum}.'
                      f"\nLet's try again, {name}!")
                break
        if operand == "-":
            sum = number - number1
            answer = prompt.string('Your answer: ')
            if answer == str(sum):
                print('Correct!')
                count = count + 1
            else:
                print(f" {answer} is wrong answer ;(. Correct answer was {sum}."
                      f"\nLet's try again, {name}!")
                break
        if operand == "*":
            sum = number * number1
            answer = prompt.string('Your answer: ')
            if answer == str(sum):
                print('Correct!')
                count = count + 1
            else:
                print(f" {answer} is wrong answer ;(. Correct answer was {sum}."
                  f"\nLet's try again, {name}!")
    if count == 3:
        print(f'Congratulations, {name}!')
