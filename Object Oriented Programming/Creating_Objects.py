# Creating Our Own Objects

class PlayerCharacter: #generally be singular (it's a blueprint)
	def __init__(self, name, age): 
# init is a special method (dunder method)
# constructor method, usually at top of class
# called anytime to call a method

# Self keyword: refers to PlayerCharacter
	# Self is the default parameter
		self.name = name
		self.age = age

	def run(self):
		print('run')
		return 'done'

player1 = PlayerCharacter('Throder', 75)
player2 = PlayerCharacter('Bradley Hidalgo Vasquez de la Rosa', 18)

print(player1.name, player1.age)
print(player1.run())
print(player2.name, player2.age)

print(player1)
print(player2)

player2.attack = 50
print(player2.attack)