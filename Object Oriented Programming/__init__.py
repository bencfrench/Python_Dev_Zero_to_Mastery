class PlayerCharacter:
	membership = True
	def __init__(self, name='anonymous', age=0):
		if age > 18:
			self.name = name
			self.age = age

	def shout(self): #method
		print(f'My name is {self.name}')

player1 = PlayerCharacter('Tom', 10)
# player2 = PlayerCharacter()

print(player1.shout())