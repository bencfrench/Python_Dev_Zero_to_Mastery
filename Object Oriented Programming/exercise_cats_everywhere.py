# Exercise: Cats Everywhere

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

tuxedo_cat = Cat('Christopher', 2)
black_cat = Cat('Maya', 4)
white_cat = Cat('JRR Tolkien', 7)

# 2 Create a function that finds the oldest cat

oldest = max(tuxedo_cat.age, black_cat.age, white_cat.age)

# 3 Print out: "The oldest cat is x years old.". x will be 
# the oldest cat age by using the function in #2

print(f'The oldest cat is {oldest} years old.')

# Instructor solution
class Cat:
	species = 'mammal'
	def __init__(self, name, age):
		self.name = name
		self.age = age

peanut = Cat('Peanut', 3)
garfield = Cat('Garfield', 5)
snickers = Cat('Snickers', 1)

def get_oldest_cat(*args): #args would be better especially if this list were to grow. any # of arguments
	return max(args)

print(f'The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.')