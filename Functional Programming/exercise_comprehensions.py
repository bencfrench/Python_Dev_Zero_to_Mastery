some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Previous exercise:
# duplicates = []
# for value in some_list:
# 	if some_list.count(value) > 1:
# 		if value not in duplicates:
# 			duplicates.append(value)

# print(duplicates)

# Using comprehensions, do this?

# my solution
duplicates = {value for value in some_list if some_list.count(value) > 1}
print(duplicates)
# instructor solution

duplicates = list({x for x in some_list if some_list.count(x) > 1})
print(duplicates) #I didn't turn the set into a list