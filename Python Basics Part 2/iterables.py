# Iterable - list, dictionary, tuple, set, string

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