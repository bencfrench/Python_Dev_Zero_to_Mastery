class PlayerCharacter:
	def __init__(self, name, age):
		self._name = first_name
		self._age = age

	def run(self):
		print('run')

	def speak(self):
		print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('ben', 27)
player1.speak() #abstraction
like (1,2,3).count() <–

# Public and Private variables
# 	Use an underscore: self._name = name
# 	But it means "don't touch this please"
# 	Python doesn't really have private variables like java