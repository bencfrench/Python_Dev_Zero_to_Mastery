# map, filter, zip, reduce

# reduce()

from functools import reduce
#import reduce() from a "tool belt" for functional tools

my_list = [1,2,3]

def double(item):
	return item * 2

def only_odd(item):
	return item % 2 != 0

def accumulator(acc, item):
	print(acc, item)
	return acc + item

print(reduce(accumulator, my_list, 0)) #6

# my_list applied to accumulator
# accumulator takes my_list
# first pass through acc is 0 (set above), item is 1
# 0 + 1
# second pass through acc is 1, item is 2
# 1 + 2
# third pass through acc is 3, item is 3
# 3 + 3
# reduced the list to data manipulated with accumulator

print(my_list) #[1, 2, 3]