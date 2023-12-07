import prompt
import random
def even():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'Answer "yes" if the number is even, otherwise answer "no"')
    count = 0
    for n in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer=prompt.string('Your answer: ') 
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
                print('Correct!')
                count +=1
    if count == 3:
                    print(f'Congratulations, {name}!')
    else:
           print (f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
even()