# allow us to use python-specific functions on objects in our class

# '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__'

# usually don't change dunder methods
# but we can do custom mods for our Classes

class Toy():
	def __init__(self, color, age):
		self.color = color
		self.age = age
		self.my_dict = {
			'name': 'yoyo',
			'has_pets': False
		}

	def __str__(self):
		return f'{self.color}'

	def __len__(self):
		return 5

	def __call__(self):
		return ('yes?')

	def __getitem__(self, i):
		return self.my_dict[i]


action_figure = Toy('red', 2)
print(action_figure.__str__())
print(str(action_figure))
print(dir(action_figure))
print(len(action_figure))
print(action_figure()) #we can just call the object itself
print(action_figure['name'])
