def welcome_user():
    print('May I have your name? ', end='')
    name = input()
    print(f'Welcome to the Brain Games!\n'
          f'May I have your name? {name}\n'
          f'Hello, {name}!')