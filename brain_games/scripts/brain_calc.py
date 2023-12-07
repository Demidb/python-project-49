import prompt
import random
def calc():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'What is the result of the expression?')
    count = 0
    for n in range(3):
        number = random.randint(1, 100)
        number1 = random.randint(1, 100)
        operand = random.choice(["+" or "-" or"*"])
        print(f'Question: {number}  {operand}  {number1}')
        answer=prompt.string('Your answer: ') 
        if operand == "+":
                sum = number + number1
        if answer == sum:
                    print('Correct!')
                    count = count + 1
        if operand == "-":
                sum = number - number1
        if answer == sum:
                    print('Correct!')
                    count = count + 1
        if operand == "*":
                sum = number * number1
        if answer == sum:
                    print('Correct!')
                    count = count + 1
    if count == 3:
                    print(f'Congratulations, {name}!')
    else:
           print (f" {answer} is wrong answer ;(. Correct answer was {sum}.\nLet's try again, {name}")
calc()