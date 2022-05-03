# Can use python documentation to get definitions
# https://docs.python.org/3/library/exceptions.html

# Error Handling
# Allows the script to keep running

#Error Handling 1
# What about handling different errors?
while True:
	try: #error handling
		age = int(input('how old are you? '))
		print(10/age)
	except ValueError: #this indicates WHICH type of error to Handle
		print('please enter a number')
		#if you have the same except block twice, 
		#it runs the first and then starts the while loop again
	except ZeroDivisionError:
		print('age must be higher than zero')
	else: #if there is no error
		print('thanks!')
		break

#Error Handling 2

def sum(num1, num2):
	try:
		return num1 + num2
	except TypeError as err: #if TypeError is caught, use type err
		print(f'please enter numbers {err}') 
		#err prints the error
	#or
	except (TypeError, ZeroDivisionError) as err:
		print('oops') #can handle multiple errors the same way

print(sum(1, '2'))

#Error Handling 3
# Sometimes, we do want the error to kill the program if severe enough

while True:
	try:
		age = int(input('what is your age?'))
		10/age
		raise ValueError('hey stop that') #throw your own errors
	except ZeroDivisionError:
		print('please enger age higher than 0')
		break
	else:
		print('thank you')
	finally:
		print('ok, I\'m done')