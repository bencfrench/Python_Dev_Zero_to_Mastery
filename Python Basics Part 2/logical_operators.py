# Logical operators

print(4 > 5)
print(4 < 5)
print(4 == 5) #not '=', which is used to assign variables
print(1 < 2 < 3 < 4)
print(1 < 2 > 4 < 3) #short circuit
print(1 >= 0)
print(1 <= 0)
print(0 != 0)
# and
# or
# not
print(not(True)) #False
print(not(False)) #True
print(not(1 == 1)) #True, but not

# is vs ==
# == checks if the values are the same
# is actually checks if the location in the memory is the same

print(True == 1)  #True; 1 converts to bool (bool(1))
print('' == 1)    #False
print([] == 1)    #False
print(10 == 10.0) #True; convert to float vice versa
print([] == [])   #True

print(True is 1) 			#False
print('1' is 1)    			#False
print([] is 1)    			#False
print(10 is 10.0) 			#False
print([1,2,3] is [1,2,3])   #False
print(True is True)			#True
print('1' is '1')			#True
print([] is [])				#False (2 dif lists)