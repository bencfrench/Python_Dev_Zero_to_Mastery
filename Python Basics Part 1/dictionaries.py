# Dictionary

dictionary = {
	'a': [1,2,3],
	'b': 'hello',
	'x': True
}
print(dictionary['b'])
print(dictionary['a'][1])

my_list = [
	{
	'a': [1,2,3],
	'b': 'hello',
	'x': True
	},
	{
	'a': [4,5,6],
	'b': 'hello',
	'x': True
	}
]
print(my_list[0]['a'][2])
print(my_list[1]['a'][2])

dictionary = {
	'weapons': [1,2,3],
	'greeting': 'hello',
	'is_Magic': True
}

# keys must be unique & immutable i.e. not lists but can be numbers, booleans, etc.

user = {
	'basket': [1,2,3],
	'greet': 'hello',
	'age': 20
}

user2 = dict(name='Johnny')
print(user.get('age',55)) #None if non-existent, #2nd is a default value

print('basket' in user)
print('age' in user.keys())
print('hello' in user.values())
print('hello' in user.items())
print(user.items())
print(user.clear())
user2 = user.copy()
print(user.pop('age'))
print(user.popitem()) #last key:value pair popped
print(user.update({'age': 55}))