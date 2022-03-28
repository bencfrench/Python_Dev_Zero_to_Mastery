#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

#loop through the list of lists.
#every 0, display an empty space
#every 1, display a *

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for i in picture:
  for x in i:
    if (x == 0):
      x = ' '
    elif (x == 1):
      x ='*'
    print(x, end='')
  print('\n') #\n adds an unnecessary line, '' is a new line

print('instructor solution')
# Instructor solution
# 1) iterate over picture
  # if 0, print ''
  # if 1, print *

for row in picture:
  for pixel in row:
    if (pixel == 1):
      print('*', end='')
    else:
      print(' ', end='')
  print('')