class User():
	def sign_in(self):
		print('logged in')

class Wizard(User):
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		print(f'attacking with power of {self.power}')

class Archer(User):
	def __init__(self, name, arrows):
		self.name = name
		self.arrows = arrows

	def check_arrows(self):
		print(f'{self.arrows} remaining')

	def run(self):
		print('ran really fast')

class Hybrid(Wizard, Archer):
	def __init__(self, name, power, arrows):
		Archer.__init__(self, name, arrows)
		Wizard.__init__(self, name, power)


hybrid1 = Hybrid('Aragorn', 50, 100)
print(hybrid1.run())
print(hybrid1.check_arrows())
print(hybrid1.attack())
print(hybrid1.sign_in())