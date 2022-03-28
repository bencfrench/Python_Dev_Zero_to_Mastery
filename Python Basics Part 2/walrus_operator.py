# walrus operator

# := is a new feature
# check what's new on python documentation

a = 'helloooooooooo'

if len(a) > 10:
	print(f'too long {len(a)} elements')
#repeating ourselves: calculating len twice

# assigning values to variables as part of larger expression
if (n := len(a)) > 10:
	print(f'too long {n} elements')

while (n := len(a)) > 1:
	print(n)
	a = a[:-1] #minus 1 operator
print(a) #h remaining