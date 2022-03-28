def say_hello():
	print('helllloooo!')
say_hello()

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
  for row in picture:
    for pixel in row:
      if (pixel == 1):
        print('*', end='')
      else:
        print(' ', end='')
    print('')

show_tree()
show_tree()
show_tree()

# (positional, default) parameters
def say_hello(name='Darth Vader', emoji=':)'): #function can receive these parameters
	print(f'helllloooo {name} {emoji}')

# (positional) arguments
say_hello('Andrei', ':)') #call, invoke the function
say_hello('Ben', ':O')
say_hello()
say_hello('Timmy')

# keyword arguments
# say_hello(emoji=':)', name='Bibi')