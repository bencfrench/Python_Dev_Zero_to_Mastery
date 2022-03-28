# functions
list()
print()
max()
min()
input()
help(input())
def my_function():
	pass

# docstrings
def test(a):
	'''
	Info: this function tests and prints param a
	'''
	print(a)
test() #now will include the comments


my_function()

# methods
. notation
'helloooo'.capitalize()
print(test.__doc__) #see help function above)
# use python documentation to search functions and methods

# clean code
def is_even(num):
	if num % 2 == 0:
		return True
	elif num % 2 != 0:
		return False

print(is_even(50))

#cleaner
def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False
print(is_even(50))

# even cleaner
def is_even(num):
	if num % 2 == 0:
		return True #since return stops the function
	return False
print(is_even(50))

# more clean
def is_even(num):
	return num % 2 == 0: #this is a boolean, True/False
print(is_even(50))