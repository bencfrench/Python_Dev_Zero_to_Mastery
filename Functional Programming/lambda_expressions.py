# lambda expressions
# one-time, anon functions you don't need more than once
# useful for functions you only use once
# anonymous functions
# don't need a name bc they don't need to be stored

# lambda parameter: action(parameter)

from functools import reduce

my_list = [1,2,3]

# def multiply_by2(item):
# 	return item * 2
# print(list(map(multiply_by2, my_list)))
# OR
print(list(map(lambda item: item*2, my_list)))
print(my_list)

# ---
# def only_odd(item):
# 	return item % 2 != 0
# OR
print(list(filter(lambda item: item % 2 != 0, my_list)))


# ---
# def accumulator(acc, item):
# 	print(acc, item)
# 	return acc + item
# OR
print(reduce(lambda acc, item: acc + item, my_list))