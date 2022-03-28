# Check for duplicates in list:

# check the list
# print whatever the duplicate values are (b and n)
# no sets
# use only conditionals and loops

#Solution removing duplicates
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
for letter in my_list:
  count = my_list.count(letter)
  if count > 1:
    my_list.remove(letter)
    print(letter, count)
print(my_list)

#Solution identifying duplicates
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for letter in my_list:
  count = my_list.count(letter)
  if count > 1:
    duplicates.append(letter)
    print(letter, count)
print(duplicates)

#Instructor Solution
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in my_list:
  if my_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)
print(duplicates)