# Scope - what variables do I have access to?
# Scope helps address limited machine resources and memory

# Order
	# 1) start with the local scope (local function)
	# 2) Parent local?
	# 3) Global scope
	# 4) built in python functions

def some_func():
	total = 100
print(total) #error: name "total" not defined

if True:
	x = 10
def some_func():
	total = 100
print(x)

a = 1
def parent():
	a = 10
	def confusion():
		return a
	return confusion()
print(a)
print(parent())

# Output:
	# 1
	# 5 - this is defined within the function, but it's still 1 in the bigger program
		# 'a' here is isolated to the function