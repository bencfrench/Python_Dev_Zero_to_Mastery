# Range: returns an object producing a sequence of integers

print(range(100)) #range(0, 100)
print(range(0, 100))

for _ in range(0, 10, 2): #'_' indicates not needed var
	print(_)

for _ in range(10, 0, -1):
	print(_)

for _ in range(2):
	print(list(range(10)))