# inheritance example
class User():
	def sign_in(self):
		print('logged in')

class Wizard(User): #inheriting the sign_in function from User
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		print(f'attacking with power of {self.power}')

class Archer(User): #child class, derived class, subclass
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		print(f'attacking with arrows. Arrows left: {self.num_arrows}')

wizard1 = Wizard('Throder', 50)
archer1 = Archer('Robin', 100)
print(wizard1.sign_in())
wizard1.attack()

# isinstance(instance, Class)
print(isinstance(wizard1, Wizard)) 	<– True
print(isinstance(wizard1, User)) 		<– True
print(isinstance(wizard1, object)) 	<– True