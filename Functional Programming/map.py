# map(), filter, zip, reduce

# map
# map(action, [1,2,3])
# map() function executes a specified function for each item in an iterable. 
# The item is sent to the function as a parameter.
def double(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return new_list

print(map(double, [1,2,3]))
# <map object at 0x109...>

def double(item):
	return (item*2)
	
print(list(map(double, [1,2,3])))
# [2, 4, 6]; also preserves original, so is pure

def double(li):
	new_list = []
	for item in li:
		new_list.append(item * 2)
	return new_list

print(double([1,2,3]))