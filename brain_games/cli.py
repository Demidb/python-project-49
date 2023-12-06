def welcome_user(name):
    print(f'Welcome to the Brain Games!\n'
          f'May I have your {name}?\n'
          f'Hello, {name}!')
    
if __name__ == "__main__":
    name = input()
    welcome_user('name')
