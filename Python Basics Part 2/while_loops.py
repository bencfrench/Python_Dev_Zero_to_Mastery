i=0
while i < 50:
	print(i)
	i += 1
	break
else: #only executes is there isn't a break
	print('done with all the work')

my_list = [1,2,3]
for item in my_list:
	print(item)

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1

while True:
	response = input('say something: ')
	if (response == 'bye'):
		break

# break, continue, and pass
my_list = [1,2,3]
for item in my_list:
	# break
	# continue #run again
	pass
	print(item)

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	# continue
	pass

# To skip for now:
my_list = [1,2,3]
for item in my_list:
	# thinking about it...
	pass

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1