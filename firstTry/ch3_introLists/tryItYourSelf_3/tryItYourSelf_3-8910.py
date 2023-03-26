# Try it Yourself 
'''
3-8. Seeing the World: Think of at least five places in the world you'd like to visit.

- a. Store the locations in a list.  Make sure the list is not in alphabetical order.

- b. Print your list in its original order.  Don't worry about printing teh list neatly, just print it as a new Python list.

- c. Use sorted() to print your list in alphabetical order without modifying the actual list.

- d. Show that your list is still in its original order by printing it.

- e. Use sorted() to print your list in reverse alphabetical order without changing the order of the original list. 

- f. Show that your list is still in its original order by printing it again.

- g. Use reverse() to change the order of your list.  Print the list to show that its order has changed.  

- h. Use reverse() to change the order of your list again.  Print the list to show it's back to its original order.

- i. Use sort() to change your list so it's stored in alphabetical order.  Print the list to show that its order has been changed. 

- j. Use sort() to change your list so it's stored in reverse alphabetical order.  Print the list to show that its order has been changed.
'''

# a. locations in a list
worldVisit = ['Egypt', 'Jamaica', 'Canada', 'Europe', 'China']

# b. print list in original order
print(worldVisit)

# c.
print("\nSorted without modifying the actual list using 'sorted(worldVisit)', temporary.\n----------------------")
print(sorted(worldVisit))

# d.
print("\nTesting ORIGINAL worldVisit is still as is after prior sort being temporary.\n----------------------------------------")
print(worldVisit)

# e. Use sorted() to print list in reverse alphabetical order without changing the order of the original list.
print("\nSorted used to print in reverse alphabetical order w/o changing original order\n---------------------")
print(sorted(worldVisit))

# e2. assigned a variable name to sorted worldVisit and printed it out
TempSortedOrder = sorted(worldVisit)
print("\nTempSortedOrder is the assigned variable to print out the sorted worldVisit\n-------------------------")
print(TempSortedOrder)

# e3. that assigned variable in reverse, not affecting the original ist
TempSortedOrder.reverse()
print(TempSortedOrder)

# f. Test to see if the original list is still in the original order
print("\nThis is the original list for worldVisit.\n---------------------------")
print(worldVisit)

# g. Use reverse() to change the order of your list.  Print the list to show that its order has changed. 
worldVisit.reverse()
print("\nThis is worldVisit.reverse() on a permanent reversal as I print out worldVisit.\n------------------------")
print(worldVisit)

# h. Use reverse() to change the order of your list again.  Print the list to show it's back to its original order. 
worldVisit.reverse()
print("\nThis is worldVisit.reverse() AGAIN on a permanent reversal as I print out worldVisit (back to original).\n------------------------")
print(worldVisit)

# i. Use sort() to change your list so it's stored in alphabetical order.  Print the list to show that its order has been changed. 
worldVisit.sort()
print("\nUsing sort() to change lsit in Alphabetical Order.\n-------------------------------")
print(worldVisit)

# j. Use sort() to change your list so it's stored in reverse alphabetical order.  Print the list to show that its order has been changed.
worldVisit.reverse()
print("Used sort() prior (making list purmanent sort), now I just reversed it.")
print(worldVisit)



'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.
'''
print("\nSee 3-6 (Prior Try It Yourself file) showing the length of people invited to dinner.")

'''
3-10. Every Function: Think of something you could store in a list.  For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.  Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
'''
print()

listOfStudyBooks = ['Craetive Illustration', 'How to Draw', 'Action Cartooning', 'Invent your Own Computer Games with Python', 'Python Crash Course']
print(listOfStudyBooks)
print("------------------------------")
# use each function introduced in the is chapter at least once.

# index position
print(listOfStudyBooks[-1])
print("------------------------------")

# individual values from list
message = f"I'm looking forward to going back over {listOfStudyBooks[3]} after studying {listOfStudyBooks[4]}."
print(message)
print("------------------------------")

#modify element from list
listOfStudyBooks[0] = 'Story'
print(listOfStudyBooks)
print("------------------------------")




# Adding Elements to a List 
# Appending Elements to the end of a List 
listOfStudyBooks = ['Craetive Illustration', 'How to Draw', 'Action Cartooning', 'Invent your Own Computer Games with Python', 'Python Crash Course']
print(listOfStudyBooks)
print("------------------------------")

listOfStudyBooks.append('Story')
print(listOfStudyBooks)
print("------------------------------")


listOfStudyBooks.append('Prepare to Board')
print(listOfStudyBooks)
print("------------------------------")


listOfStudyBooks.append('Successful Drawing')
print(listOfStudyBooks)
print("------------------------------")



# Inserting Elements into a List
listOfStudyBooks.insert(3, 'You Can Draw')
print(listOfStudyBooks)
print("------------------------------")


# Removing Elements from a List
# using the del Statement
del listOfStudyBooks[-2]			# 2ND TO LAST ON THE LIST
print(listOfStudyBooks) 	
print("------------------------------")



# Removing Item using the pop() Method
popped_listOfStudyBooks = listOfStudyBooks.pop(4)
print(listOfStudyBooks)
print(popped_listOfStudyBooks)
print("------------------------------")


# Removing Item by Value
listOfStudyBooks.remove('Action Cartooning')
print(listOfStudyBooks)
print("------------------------------")



# Organizing a List
# Sorting a List Permanently with the sort() Method
listOfStudyBooks.sort()
print(listOfStudyBooks)
print("------------------------------")



# Sorting a List Temporarily with the sorted() Function
listOfStudyBooks = ['Craetive Illustration', 'How to Draw', 'Action Cartooning', 'Invent your Own Computer Games with Python', 'Python Crash Course']
print(listOfStudyBooks)

print("\n----------------Here is the TEMPORARY saorted() version of the list")
print(sorted(listOfStudyBooks))

print("\n----------------and here is the ORIGINAL list (not affected by sorted() function prior)")
print(listOfStudyBooks)

print("------------------------------")


# Printing a LIst in Reverse Order
listOfStudyBooks.reverse()
print(listOfStudyBooks)
print("------------------------------")


# Finding the Length of a List
print(len(listOfStudyBooks))
print(f"So far {len(listOfStudyBooks)} is just a fraction of Boooks I have as Reference.")
