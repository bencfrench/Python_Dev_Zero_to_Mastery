print(type("hey hello there 24!"))

username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
O.O
---
''' #multi-line strings

print(long_string)

first_name = 'Andrei'
last_name = 'Neogoie'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation
print('hello' + ' Andrei')

# Type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape sequences
weather = "\tIt\'s \"kind of\" sunny. \n hope you have a good day!" 
#\ = what follows is a string
#\t = add a tab space
#\n = new line
print(weather)

# Formatted strings
name = 'Johnny'
age = 55
print('Hi, ' + name + '. You are ' + str(age) + ' years old.')
# or
print(f'hi {name}. You are {age} years old') #f = formatted string
# or
print('hi {}. You are {} years old'.format(name, age))
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))

# String indexes
selfish = '01234567'
# 		   01234567
# [start:stop:stepover]
print(selfish[0])
print(selfish[0:8:2])
print(selfish[-1]) #start at end of string
print(selfish[::-1]) #step over from the back

# methods
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote) #immutability