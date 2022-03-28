# check if magician AND expert: 
# 'you are a master magician' if both true

# check if magicianbut not expert:
# 'you're getting there'

# if not a magician:
# 'you need magic powers'

is_magician = False
is_expert = True

if is_magician and is_expert:
	print('You are a master magician')
elif is_magician and not is_expert:
	print('You\'re getting there')
elif not is_magician:
	print('You need magic powers')


# Instructor solution: same as mine!
# if is_expert and is_magician:
# 	print('You are a master magician')
# elif is_magician and not is_expert:
# 	print('at least you\'re getting there')
# elif not is_magician:
# 	print('You need magic powers')