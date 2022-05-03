while True:
	try:
		age = int(input('how old are you? '))
		10/age
	except ValueError:
		print('please enter a number')
		continue
	except ZeroDivisionError:
		print('age must be higher than 0')
		break
	else:
		print('thanks!')
		break
	finally: # always prints at the end
		print('ok, I\'m finally done')
	print('can you hear me?')

# ZeroDivisionError: prints that except block and the finally block
# ValueError: prints that except block and the finally block, starts loop over
# No error: returns, thanks, & the finally block. it breaks, except for the finally block