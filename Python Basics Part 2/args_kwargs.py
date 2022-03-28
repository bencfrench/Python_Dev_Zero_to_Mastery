# *args and **kwargs
# arguments and keyword arguments
def super_func(*args, **kwargs): #*: this can accept any number of arguments
	print(*args)
	print(args)
	print(kwargs)
	total = 0
	for items in kwargs.values():
		total += items
	return sum(args) + total	kwargs

super_func(1,2,3,4,5, num1=5, num2=18)
#RULE: params, *args, default params, **kwargs
# ex. def super_func(name, *args, i='hi', **kwargs):