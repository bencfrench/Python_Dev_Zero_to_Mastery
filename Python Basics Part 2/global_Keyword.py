# global Keyword

total = 0

def count():
	total += 1 #error - count doesn't know total from the "outside world"
	return total

print(count())

def count():
	global total 
	total += 1
	return total
count()
count()
print(count())
print(total) #this changes the global total

# dependency injection
def count(total):
	total += 1
	return total

count(total)
count(total)
print(count(total)) #does not change global total
print(count(count(count(total))))