# Changing, Adding, and Removing Elements
print("# Changing, Adding, and Removing Elements\n")

# Modify Elements in a list. --> motorcycles = ['honda', 'yamaha', 'suzuki']
print("\n# Modify Elements in a list. \n--> motorcycles = ")
print("-------------------------------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# changes the value of the first item, the rest of the list stays the same 
# you can change the value of any item on the list
print("\n\nModify Elements in a List\n-----------------------------") 
motorcycles[0] = 'ducati'
print(motorcycles)


# Adding Elements to a List
# Appending Elements to the End of a List  --> motorcycles.append('ducati')
print("\n# Appending Elements to the End of a List  \n--> motorcycles.append('ducati')")
print("-------------------------------------------")
motorcycles.append('ducati')
print(motorcycles)


# Inserting Elements into a List
print("\n# Inserting Elements into a List...  \n-->  motorcycles.insert(0, 'kingzlofitness')")
print("-------------------------------------------")
motorcycles.insert(0, 'kingzlofitness')
print(motorcycles)


# Removing an Item Using the del Statement
print("\n# Removing an Item Using the del Statement")
print("del motorcycles[0] &")
print("del motorcycles[1]")
print("-------------------------------------------")
del motorcycles[0]
print(motorcycles)


del motorcycles[1]
print(motorcycles)



# Removing an Item Using the pop() Method
# somethimes you'll want to use the value of an item after you remove it from a list33
# the pop() method removes the last item in a list, but it lets you work with that itme after removing it
print("\n# Removing an Item Using the pop() Method")
print("-------------------------------------------")
print("original Items")
print(motorcycles)

print("\n")
# pop a value from the list and store (assign) in the variable popped_motorcycle
popped_motorcycle = motorcycles.pop()
# print the list to show that a value has been removed from the list
print(motorcycles)
# print the popped value.  to prove we still have access to the value that was removed
print(popped_motorcycle)



# imagine that the motocycles in the list are stored in chronological order according to when we owned them 
# example to print a statement about the last motocycle we bought
print()
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
last_owned = motocycles.pop()
print(f"The last motocycle I owned was a {last_owned.title()}.")




# Popping itmes from any Position in a List
# you can use pop() to remove an item from any positon in a list by including the index of the item you want to ermove in parentheses
print()
print("- Popping items from any Position in a List")
first_owned = motocycles.pop(0)
print(f"The first motocycle I owned was a {first_owned.title()}.")






# Removing an Item by Value
# sometimes you won't know the position of the value you want to remove from a list.
# if you only know the value of the item you want to remove, you can use remove() method
print("\n\n\nRemoving an Item by Value\n--------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# remove the value (element) 'ducati' 
motorcycles.remove('ducati')
print(motorcycles)



print('\n\n\n')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# you can also use the remove() method to work with a value that's being removed from a list 
# assign the value 'ducati' to a variable called too_expensive
too_expensive = 'ducati'
# we then use this variable to tell Python which value to remove from the list
motorcycles.remove(too_expensive)
print(motorcycles)

print(f"\nA {too_expensive.title()} is too expensive for me.")




'''
NOTE: remove() method delets only the first occurrence of the value to specify
- there's a possibility the value appears more than once in the list
- you'll need to use a loop to make sure all occurrences of the value are removed 
- you'll learned how to do this in Chapter 7
'''

