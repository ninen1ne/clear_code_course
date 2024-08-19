# 16/7/2024 - Norawee 
""" 
	Methods are functions that are attached to objects(OOP)
	to called method | method_name(arg1, arg2, ..., arg_n)

	what it's mean by attached to obj when you've create an instance like dog1
	to use method that attached to dog1 obj we will use '.' (a dot)  | dog1.method_name(arg1, ..., arg_n)
"""

test = 'A word'.upper() # .upper() is a method 
print(test) # or print(test.upper())

username = 'JOhn SmIthXX'
print(username.title().strip('x'))
# clean our data by called chain methods it will execute from left to right 

print(dir(username))

print(username.isalpha()) # return false because spacebar not is an alphabet

# exercise 
exercise_string = 'I like puppies'
new_exercise_string = exercise_string.replace('puppies', 'kittens')
print(new_exercise_string)