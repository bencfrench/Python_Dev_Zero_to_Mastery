# map(), filter, zip, reduce

# filter()
# can receive less than we give

my_list = [1,2,3]
def double(item):
	return item * 2

def only_odd(item):
	return item % 2 != 0

print(list(filter(only_odd, my_list))) #[1, 3]
print(my_list) #[1, 2, 3]