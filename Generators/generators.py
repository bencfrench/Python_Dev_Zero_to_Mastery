# Generators
# Allow us to generate a sequence of values over time

# Allows us to use keyword 'yield' to pause/resume generation

# range(100) (not held in memory)
# range() is just a generator, not held in memory

# list(range(100)) (held in memory)

# def make_list(num):
# 	result = []
# 	for i in range(num):
# 		result.append(i*2)
# 	return result

# my_list = make_list(100) - my_list pointing to a location in memory.
# print(my_list)

# iterable - any object we can loop through (dunder: __iter__ method)
#    generators ARE iterable

def generator_function(num):
	for i in range(num):
		yield i*2
# yield: pauses the function, and comes back to it when you use 'next'

for item in generator_function(1000):
	print(item) #yield stops it each item

g = generator_function(100)
print(g) #<generator object at ...>
# print(next(g)) - returns 0
next(g)
next(g)
print(next(g)) # goes 0, 1*2, 2*2 = '4'
print(next(g)) # 3*2 = 6

# yield only keeps the most recent data in memory
# therefore, yield makes it a generator