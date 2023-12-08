import prompt
import random

def gcd():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'Find the greatest common divisor of given numbers.')
    count = 0
    for n in range(3):
        number = random.randint(1, 100)
        number1 = random.randint(1, 100)
        print(f'Question: {number} {number1}')
        answer=prompt.string('Your answer: ') 
        true_answer = delitel
        if answer == true_answer:
                print('Correct!')
                count +=1
    if count == 3:
                    print(f'Congratulations, {name}!')
    else:
           print (f"{answer} is wrong answer ;(. Correct answer was {true_answer}.\nLet's try again, {name}")

def delitel():
    number = a
    number1 = b
    while a != 0 and b != 0:
        if a > b:
                a = a % b
        else:
            b = b % a
    return a + b

            
        
gcd()