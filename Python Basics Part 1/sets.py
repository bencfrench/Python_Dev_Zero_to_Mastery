# Set
# unordered collections of unique objects

my_set = {1,2,3,4,5,5}
print(my_set) #won't add the second 5. must be unique.

my_set.add(100) #unique, will add
my_set.add(2) #already contains this, won't add

my_list = [1,2,3,4,5,5]
print(my_list)
print(set(my_list)) #remove duplicates

my_set = {1,2,3,4,5,5}
print(my_set[0]) #not index, must do value
print(1 in my_set)
print(len(my_set))
print(list(my_set))

new_set = my_set.copy()
print(new_set)

.difference()
.discard()
.difference_update()
.intersection()
.isdisjoint()
.issubset()
.issuperset()
.union()

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
print(my_set.discard(5)) #None
print(my_set) #{1, 2, 3, 4}
print(my_set.difference_update(your_set))
print(my_set.intersection(your_set))
# Shorthand version: print(my_set & your_set)
print(my_set.isdisjoint(your_set)) #do they have any common values?
print(my_set.union(your_set))
# Shorthand version: print(my_set | your_set)
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))