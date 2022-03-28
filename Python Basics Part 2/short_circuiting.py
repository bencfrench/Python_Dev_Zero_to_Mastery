is_Friend = True
is_User = True

if is_Friend or is_User:
	print('bffs') 
# if the first condition is true it doesn't 
# need to evaluate the second
# So it short-circuits in that case, more efficient