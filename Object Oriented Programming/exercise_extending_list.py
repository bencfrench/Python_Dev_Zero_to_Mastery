# Create a super list
	# add code that allows us to
	# access through index (any list)
	# will have a special dunder method always return 1000
	# inheritance, OOP

class SuperList(list):
	def __len__(self):
		return 1000

super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])

#double check
print(issubclass(SuperList, list)) #True
print(issubclass(SuperList, object)) #True