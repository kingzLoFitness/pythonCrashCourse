# introducing Lists

# What is a List?
# bicycles.py
bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles)


print(bicycles[0])


print(bicycles[0].title())



# Index Position Start at 0, Not 1

print(bicycles[1])
print(bicycles[3])

# last item on the list
print(bicycles[-1])



# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

'''
# Try it Yourself 
3-1. Names:

3-2. Greetings:

3-3. Your Own List:
'''

# Changing, Adding, and Removing Elements



print()

# Modifying Elements in a List

#motorcycles.py
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)


motorcycles[0] = 'ducati'
print(motorcycles)



# Adding Elements to a List
# Appending Elements to the End of a List

motorcycles.append('ducati')
print(motorcycles)


# Append from an Empty List
cars = []

print(cars)

cars.append('honda')
print(cars)

cars.append("BMW")
print(cars)

cars.append("Jeep")
print(cars)

cars.append("Tesla")
print(cars)


print()
# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)



print()
# Removing Elements from a List
del motorcycles[0]
print(motorcycles)


del motorcycles[1]
print(motorcycles)


print()
# Removing an Item Using the pop() Method - last item in first example
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)


print()
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")



# Popping Items from any Position in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


print()
# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'sazuki', 'ducati']
print(motorcycles)


# motorcycles.remove('ducati')
removed_motorcycle = motorcycles.remove('ducati')
print(motorcycles)
print(f"Removed motocycle was {removed_motorcycle}.")

# I did the above from Scratch, but it didn't work as I wanted 
# The output came out as none. 



# Here we go with it more by the book
print("\n# Removing an Item by Value")


###########################################################
###########################################################
###########################################################

# Removing an Item by Value 
print(motorcycles)

motorcycles.append("Tern")
print(motorcycles)


# my Example, not as accurate though
not_a_motorcycle = motorcycles.remove("Tern")
print(not_a_motorcycle)

print(f"\n{motorcycles}")

# this example is more accurate 
motorcycles.append("ducati")
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")




''' 
Try it Yourself page 42
3-4 Guest List:

3-5. Changing Guest List:

3-6. More Guests:
'''


###########################################################
###########################################################
###########################################################
print()


# Organizing a List
# Sorting a List Permanently with the sort() Method
# cars.property

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

# like it is Permanently set
cars.sort(reverse=True)
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
# Sorting a List Temporarily with the sorted() Function
print("\nHere is the original list:")
print(cars)


print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


# Printing a List in Reverse Order
cars.reverse()
print(cars)


# Finding the Length of a List
print(len(cars))



"""
Try it Yourself page 46 
3-8.  Seeing the World

3-9.  Dinning Guests

3-10. Every Function:

"""


'''
# Avoiding Index Errors When Working with Lists
# motorcycles.py
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

output:
IndexError: list index out of range
'''


'''
Try it Yourself page 47
3-11. Intentional Error:

'''


