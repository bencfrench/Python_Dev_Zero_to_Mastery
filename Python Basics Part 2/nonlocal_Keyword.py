#nonlocal Keyword

# nonlocal is used to refer to the parent local, but not global
# generally might be needlessly complicated
x = 'global'
def outer():
	x = 'local'
	def inner():
		nonlocal x
		x = 'nonlocal'
		print('inner:', x)

	inner()
	print('outer:', x)

outer()
print(x) #global

# 1 - start with nonlocal
# 2 - parent nonlocal
# 3 - global
