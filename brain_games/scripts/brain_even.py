import prompt
import random
def even():
    print(f'Answer "yes" if the number is even, otherwise answer "no"')
    count = 0
    for n in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input()
        print(f'Your answer: {answer}')
        if number % 2 == 0 :
                print('Correct!')
                count +=1
    if count == 3:
                    print(f'Congratulations, {name}!')
    print (f"'yes' is wrong answer ;(. Correct answer was 'no'./nLet's try again, {name}")
