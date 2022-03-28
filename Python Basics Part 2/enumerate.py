# Enumerate - returns index too

for i,char in enumerate('Helllooo'):
	print(char, i)

for i,char in enumerate([1,2,3]):
	print(i, char)

for i,char in enumerate((1,2,3)):
	print(i, char)

#script that enumerates a list of numbers
for i,char in enumerate(list(range(100))):
	if char == 50:
		print(f'index of 50 is: {i}')