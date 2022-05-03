# for loop example
def special_for(iterable):
	iterator = iter(iterable) #iter: we can use next function
	while True:
		try:
			print(iterator)
			print(next(iterator)*2)
		except StopIteration: #exception type
			break

special_for([1,2,3]) #same memory space for all!

# DIY range example
class MyGen():
	current = 0
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def __iter__(self):
		return self

	def __next__(self):
		if MyGen.current < self.last:
			num = MyGen.current
			MyGen.current +=1
			return num
		raise StopIteration

gen = MyGen(0,100)
for i in gen:
	print(i)