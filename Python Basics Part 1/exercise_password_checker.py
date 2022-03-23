username = input('What is your username? ')
password = input('What is your password? ')
length = len(password)
password_hide = '*' * length
print(f'{username}, your password, {password_hide}, is {length} characters long. :)')