# 16/7/2024 - Norawee
""" 
	Return is a glue that connects everything in python 

	Any operation returns a value 2 + 2, return a value(4 in this case)
	Functions & Methods also return values 
	.upper() returns uppercase of a string 

	abs(len('a word')* -10) first len() return integer value then abs return absolute value 
"""
print(abs(len('a word')* -10)) # abs(6 * -10) = abs(-60) = 60

test_variable = len('A word'.upper().replace('A', 'X'))
print(test_variable)