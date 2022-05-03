class PlayerCharacter:
	membership = True # Class Object Attribute | static
	def __init__(self, name, age):
		if self.membership:
		#OR: if PlayerCharacter.membership:
			self.name = name
			self.age = age

	def shout(self): #method
		print(f'My name is {self.name}')
		return 'done'

	def run(self, hello):
		print(f'my name is {self.name}')

player1 = PlayerCharacter('Throder', 75)
player2 = PlayerCharacter('YikYelk', 8)
player2.attack = 50

print(player2.membership)
print(player2.name)
print(player1.shout())
print(player2.shout())
print(player2.run('greetings'))