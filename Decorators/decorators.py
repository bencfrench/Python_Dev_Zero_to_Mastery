# @classmethod
# @staticmethod

# Decorators: @<name>

# functions are "first-class citizens" – act just like variables
# def hello():
# 	print('hello');

# greet = hello
# del hello
# hello() #traceback
# print(greet()) #greet still points to the function hello(), even if hello is deleted

# def hello(func):
# 	func()

# def greet():
# 	print('still here!')

# a = hello(greet) #don't have to call it with () because hello() calls it
# print(a)

# Higher Order Function (HOC)
# a function that accepts another
# a function that returns another 
# def greet(func):
# 	func()

# def greet2():
# 	def func():
# 		return 5
# 	retun func

# decorators add featuers to functions
# a function that wraps another function and enhances it

# Decorator Pattern. a famous pattern in coding
def my_decorator(func):
	def wrap_func(*args, **kwargs):
		print('*********')
		func(*args, **kwargs)
		print('*********')
	return wrap_func

@my_decorator
def hello(greeting, emoji=':O'):
	print(greeting, emoji)

hello('hi big guy')

# Wrapping hello() with the decorator