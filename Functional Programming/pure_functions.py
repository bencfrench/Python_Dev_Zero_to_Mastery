def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item*2)
	return new_list

print(multiply_by2([1,2,3]))

# Is this a pure function?
# 1) Given the same input, it always returns the same output
# 2) Produces no side effects to 'outside world'
# 	- if we returned print() that would have side effects (using print)
# 	- if new_list was defined outside, that would have side effects too
# 	- ideally contain the functions to keep pure