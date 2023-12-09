import prompt
import random


def generate_question():
    number = random.randint(1, 100)
    number1 = random.randint(1, 100)
    operand = random.choice(["+", "-", "*"])
    return number, number1, operand


def get_useranswer():
    return prompt.string('Your answer: ')


def main():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'What is the result of the expression?')
    count = 0
    for n in range(3):
        number, number1, operand = generate_question()
        print(f'Question: {number} {operand} {number1}')

        if operand == "+":
            result = number + number1
        elif operand == "-":
            result = number - number1
        else:
            result = number * number1

        answer = get_useranswer()

        if answer == str(result):
            print('Correct!')
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}.'
                  f"\nLet's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
