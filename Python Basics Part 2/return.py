def sum(num1, num2):
	return num1 + num2 #functions must return something

total = sum(10,5)
print(sum(4,total))

# another example
def sum(num1, num2):
	def another_func(n1, n2):
		return n1 + n2
	return another_func(num1, num2)

total = sum(10,20)
print(total)

# return automatically exits the function