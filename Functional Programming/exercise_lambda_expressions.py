# List Square
# square our list
# one line that will print the squared list
my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))

# List Sorting
# sort based on the second value only
a = [(0,2), (4,3), (9,9), (10,-1)]
print(sorted(a, key=lambda x: x[1])) #this preserves the list as is
print(a)

# Modify list
a.sort(key=lambda x: x[1])
print(a)