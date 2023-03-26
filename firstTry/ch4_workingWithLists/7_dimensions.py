'''
Tuples
(to me are like constants)
- list of items that cannot change
- values that cannot change are immutable (aka a tuple)
'''


'''
Defining a Tuple
- two parentheses instead of the square brackets
'''
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


'''
If you try to change one of the items in the tuple dimensions:

EXAMPLE:
dimensions[0] = 250

This is the OUTPUT:
TypeError
'tuple' object does not support item assigment 
'''



'''
NOTE: tuple with one element, you need to include a trailing comma:

In addition (what they said) it doesnt often make sense to bulid a tuple with one element. 
- But this can happen when tuples are generated automantically.
'''
my_t = (3,)









print()
'''
Looping through all Values in a Tuple
- using a for loop, just as you did with a list.
'''

for dimension in dimensions:
	print(dimension)








print()
'''
Writing over a Tuple
- redefine the entire tuple
- no errors this time because 'reasigning' a variable is valid
'''

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
	

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)


'''
When compared with lists, tuples are simple data sctructures 
- a set of values that should not be changed throughout the life of a program
'''

