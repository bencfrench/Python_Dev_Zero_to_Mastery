li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2.5,'a', True]

# List slicing
string = 'helllooo'
print(string[0:2:1])

amazon_cart = [
	'notebooks', 
	'sunglasses',
	'toys',
	'grapes'
]

amazon_cart[0] = 'Macbook Pro'
print(amazon_cart[0:2])
print(amazon_cart[0::2]) # step over by 2
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Making new_cart = amazon_cart would mean that changes to new_cart is amazon_cart. so changes to new_cart would cause changes to amazon_cart.
# Instead, use new_cart = amazon_cart[:] to make a copy of amazon_cart

# Matrix = 2D array

matrix = [
	[1,5,3],
	[2,4,6],
	[7,8,9]
]
print(matrix[0][0:2])

# List Methods (methods are specific to a data type)
basket = [1,2,3,4,5]
print(len(basket))

#adding
basket.append(100)
basket.insert(4, 100)
basket.extend([100, 101])

#removing
basket.pop() #removes last item
basket.pop(0) #removes indexed item
basket.remove(4)
basket.clear()

basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('b', 0, 3))
print('d' in basket) #true
print(basket.count('d'))

# basket.sort()
# sorted(basket)
# print(basket)
print(sorted(basket)) #new array, preserves basket
new_basket = basket.copy()
basket.reverse()

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
# print(basket[::-1])
# print(basket)

print(list(range(1,100)))
print(list(range(100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'jojo'])
print(new_sentence)
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jojo'])

# list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)