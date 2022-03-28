# Exercise: Functions
# use the function to find and print the highest even in the list

#My solution
def highest_even(li):
  li.sort(reverse=True)
  for item in li:
    if item % 2 == 0:
      return item

print(highest_even([2,10,1,2,3,4,8,11]))

#Instructor solution:
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8,11]))