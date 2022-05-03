class PlayerCharacter:
	membership = True
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def shout(self):
		print(f'my name is {self.name}')

	@classmethod #decorator
	def adding_things(cls, num1, num2): #cls is class #dont need to instantiate
		return cls('Teddy', num1 + num2) #instantiate teddy
	# this is a method on the actual class

	@staticmethod
	def adding_things2(num1, num2):
		return num1 + num2

player1 = PlayerCharacter('Throder', 74)

print(player1.shout())
player3 = PlayerCharacter.adding_things(2,3)
print(player3.shout())

print(PlayerCharacter.adding_things2(3,6))