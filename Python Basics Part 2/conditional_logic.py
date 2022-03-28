# Conditional Logic
is_old = True
is_licensed = True

if is_old:
	print('you are old enough to drive!')
elif is_licensed:
	print('you can drive now!')
else:
	print('you are too young to drive!')

if is_old and is_licensed:
	print('you are old enough, and you have a license!')
else:
	print('you are not of age!')

print('alright alright alright')

is_old = bool('hello') #returns True; '' returns False
is_licensed = bool(5) #returns True; 0 returns False
# Python converts values to booleans 

password = '123'
username = 'johnny'

if password and username:
	print('your profile is complete!')

# Ternary Operator

# condition_if_true if condition else condition_if_else
# If condition is true, condition_if_true; otherwise, condition_if_else

is_friend = True
can_message = 'message allowed' if is_friend else 'cannot message'
print(can_message)