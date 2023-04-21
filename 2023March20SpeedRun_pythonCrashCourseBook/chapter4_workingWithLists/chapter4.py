# Looping through an Entire List

# magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# A Closer Look at Looping



print()
# Doing More Work Within a for Loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing something after the for loop
print("Thank you, everyone.  That was a great magic show!")


"""
Try it Yourself page 56
4-1. Pizzas

4-2. Animals
"""

###########################################################
###########################################################
###########################################################



# Making Numerical Lists
# Using the range() Function
# first_numbers.py

for value in range(1, 5):
    print(value)


# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)



# even_numbers.py
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# squares.py
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)




# squares.py
squares = []
for value in range(1, 11):
    # this 1 line of code does the same as above
    squares.append(value ** 2)

print(squares)



print()
# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)

print(min(digits))

print(max(digits))

print(sum(digits))



# List Comprehensions
# squares.py
# 
# the for loop in this example is for value in range (1, 11), which feeds the values 1-10 into the expression value**2
squares = [value**2 for value in range(1, 11)]
print(squares)

# PRACTICE to CREATE List Comprehensions



"""
Try it Yourself
4-3. Counting to Twenty:

4-4. One Million:

4-5. Summing a Million:

4-6. Odd Numbers:

4-7. Threes:

4-8. Cubes:

4-9. Cube Comprehension:

"""




###########################################################
###########################################################
###########################################################



# Working with Part of a List
# Slicing a List

# players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# to output the first three elements in a list
# - request indices0 through 3
# - would return elements 0, 1, and 2
print(players[0:3])


# start slice at index 1 and end at index 4
print(players[1:4])



# if you omit the first index in a slice, Python automatically starts your slice at the BEGINNING of the list
print(players[:4])


# similar syntax, if you want a slice that includes the END of a list
# third item through the last item
# start with index 2 and omit the second index
print(players[2:])



# this prints all items from the third item through the end of the list
print(players[-3:])


# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


print()
# Copying a List
# foods.py 
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

"""
This doesn't Work:
friend_foods = my_foods

it would cause both variables to point to the same list
"""

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


# proof that we have 2 separate lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)




'''
Try it Yourself page 65
4-10. Slices

4-11. My Pizzas, Your Pizzas

4-12 More Loops:

'''



###########################################################
###########################################################
###########################################################


print()
# Tuples - list of items that cannot change (immutable)


# Defining a Tuple (like a list, but with parenthesis instead of brackets)

# dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


"""
dimensions[0] = 250

TypeError: 'tuple' object does not support item assignment
"""
print(dimensions)


# a tuple with one element
my_t = (3,)
print(my_t)




# Looping Through All Valuse in a Tuple
for dimension in dimensions:
    print(dimension)

print()
# Writting over a Tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)