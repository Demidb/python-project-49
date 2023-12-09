import prompt
import random


def main():
    def hidden_number(progression):
        hidden_index = random.randint(0, len(progression) - 1)
        true_hidden = progression[hidden_index]
        progression[hidden_index] = ".."
        return progression, true_hidden

    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f"Hello, {name}!\n"
          f'What number is missing in the progression?')
    count = 0
    for n in range(3):
        length = random.randint(5, 10)
        step = random.randint(1, 10)
        first_number = random.randint(0, 100)
        progression_list = [first_number + i * step for i in range(length)]
        hidden_prog, hidden_number_value = hidden_number(progression_list)
        print("Question:", " ".join(map(str, hidden_prog)))
        answer = prompt.string('Your answer: ')
        true_answer = str(hidden_number_value)

        if answer == true_answer:
            print('Correct!')
            count += 1
        else:
            print(f" {answer} is wrong answer ;(. "
                  f"Correct answer was {true_answer}."
                  f"\nLet's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
        pass
