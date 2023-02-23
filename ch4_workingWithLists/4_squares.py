squares = []

for value in range(1, 11): 
	# in Python, two asterisks (**) represent expontents
	# the current value is raised to the second power
	square = value ** 2
	# each new value of square is appended to the list squares
	squares.append(square)

# when the loop has finished running, the list of squares is printed 
# the printout: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)





print()

squares = []
for value in range(1, 11):
	# same as above,  htis time each value in the loop is raised ott he second power and then immediately appended to the list of squares
	squares.append(value**2)
	
print(squares)




print()
'''
Simple Statistics with a List of Numbers
- a few Python functions are helpful when working with lists of numbers.  
'''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]



print("This is the min of Digits:")
print(min(digits))


print("This is the max of Digits:")
print(max(digits))

print("This is the sum of Digits:")
print(sum(digits))





print()
'''
List Comprehensions
- earlier described earlier for generating the list squares consisted of using there or four lines of code.  
- A list comprehension allows you to generate this same list in just one line of code. 
- A list comprehension combines the for loop and the craetion of new elements into one line, 
-- and automatically appends each new elements
= not always presented to beginners
- but because you'll most likely see them as soon as you start looking at other people's code
'''

squares = [value**2 for value in range(1, 11)]
print(squares)
