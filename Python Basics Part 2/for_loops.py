# For loops
#for SOMETHING in an ITERABLE:
for item in 'Zero to Mastery': #string
	print(item)
	print(item)

for item in [1,2,3,4,5]: #list
	print(item)

for item in {1,2,3,4,5}: #set
	print(item)

for item in (1,2,3,4,5): #tuple
	print(item)
print(item) #will print 5, because 
# the for loop goes through the iterable

for item in (1,2,3,4,5):
	for x in ['a', 'b', 'c']:
		print(item, x)

user = {
	'name': 'Gollum',
	'age': 5006,
	'can_swim' = False
}

for item in user:
	print(item) # prints the keys

for item in user.items():
	print(item) # prints the tuples

for item in user.values():
	print(item) # prints the values

for item in user.keys():
	print(item) # prints the keys

for item in user.item():
	key, value = item;
	print(key, value) # prints key and value not in tuple

for key, value in user.items():
	print(key, value) # prints key and value not in tuple