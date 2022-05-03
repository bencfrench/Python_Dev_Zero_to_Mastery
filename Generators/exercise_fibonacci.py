# My solution
def fib():
	x, y = 0, 1
	while True:
		yield x
		x, y = y, x + y

f = fib()
for i in range(21):
	print(next(f))

# Instructor solution
def fib(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b
		b = temp + b

for x in fib(30):
	print(x)

# As a list
def fib2(number):
	a = 0
	b = 1
	result = []
	for i in range(number):
		result.append(a)
		temp = a
		a = b
		b = temp + b
	return result

print(fib2(21))