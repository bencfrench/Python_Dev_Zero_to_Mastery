class User(object):
	def __init__(self, email):
		self.email = email

	def sign_in(self):
		print('logged in')


class Wizard(User): #call User when we instantiate wizard1
	def __init__(self, name, power, email):
		User.__init__(self, email)
		# OR
		# super().__init__(mail) <– don't need self
		self.name = name
		self.power = power

	def attack(self):
		# User.attack(self)
		print(f'attacking with power of {self.power}')

# introspection - identifying an object at runtime
#print(dir(wizard1))
wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)
print(dir(wizard1))