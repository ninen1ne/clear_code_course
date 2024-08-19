# 16/7/2024 - Norawee
""" 
	function are special command in python it's a block of code 
	that should does a one specific job 

	benefits of using func: 
	1) you don't have to rewrite the same logic code everytimes.
	2) it's organize your program

	print() also function that print 'text'

	called func: func(argument1, argument2) ;
	 when you've called function python will execute code in side func
"""

print('test')
word_length =len('another word')
print(word_length)

print(abs(-50))
print('one argument', 'another argument', 'another argument', 'another argument')

# max()
""" 
	The max() function returns the item with the highest value, or the item with the
	highest value in an iterable.
	If the values are strings, an alphabetically comparison is done.
"""
animals = ['dog', 'cat', 'monkey'] # for string the longest one will be return
animals_max = max(animals)
print(animals_max)

numbers = [1, 2, 3, 7, 6, 3, 8]
max_number = max(numbers)
print(max_number)

print(max(1, 5, 2, 8, 10, 11, 9))

