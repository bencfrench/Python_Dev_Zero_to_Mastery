# counter
# count items in a list

# use looping to loop over the list iterable 
# and sum the total

my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for x in my_list:
  sum += x
print(sum)

#instructor solution
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
	counter = counter + item
print(counter)