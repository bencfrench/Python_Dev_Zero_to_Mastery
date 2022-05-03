# map, filter, zip, reduce

# zip()
# zip two lists/iterables together

my_list = [1,2,3]
your_list = [10,20,30]
their_list = (3,4,5) #even works with other types (tuples)
def double(item):
	return item * 2

def only_odd(item):
	return item % 2 != 0

print(list(zip(my_list, your_list, their_list))) #[(1, 10, 3), (2, 20, 4), (3, 30, 5)]
print(my_list) #[1, 2, 3]