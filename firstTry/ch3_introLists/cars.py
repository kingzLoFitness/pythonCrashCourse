'''
Organizing a List

- lists will be created in an unpredictable order
- you cant always control the order in which your users provide their data

- you'll frequently want to preserve the original order of your list, 
- and other times you'll want to change the original order.

Python provides a a number of different aways to organize your lists, depending on the situation.
'''

# Sorting a List Permanently with the sort() Method

# regular ordered list
cars =  ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# Sorted List from Alphabetical order PERMANENTLY.  Not being able to revert to the original order
cars.sort()
print("\nSorted List Alphabetically PERMANENTLY\n--------------------------------------")
print(cars)



print("\n\n")
'''
# Sorting a List Temporarily with the sorted() Funciton
# to maintain the original order of a list but present it in a sorted order
'''

cars =  ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

# display your list in a sorted order temporarily, use sorted() function
print("\nHere is the (temporary) sorted list using sorted() function:")
print(sorted(cars))


print("\nHere is the original list again:")
print(cars)

# end 





print("\n\n")
''' 
# Printing a list in Reverse Order
- to reverse the original order of a list, use the reverse() method
- reverse chronological order

- Notice that reverse() doesn't sort backward alphabetically, 
- it simply reversae the order of the list 
- PERMANENTLY
'''

cars =  ['bmw', 'audi', 'toyota', 'subaru']
print("Regular order of Cars\n------------------")
print(cars)

# the reverse() method changes the order of a list PERMANENTLY, 
# but you can revert tot he original order anytime by applying reverse() to the same list a second time
cars.reverse()
print("\nReverse Order\n------------")
print(cars)


print("\nReversed Back to Original Order\n----------")
cars.reverse()
print(cars) 



# end
print("\n")

'''
Finding the Length of a List
- simply by using the len() function
'''
print(f"We have {len(cars)} cars at my house.")
print("Using the len() function to get the number of items ")
print(len(cars))



'''
You'll find len() useful 
- when you need to identify the number of aliens that still need to be shot down in a game
- determine the amount of data you have to manage in a visualization 
- or figure out the number of registered users on a website
- amung other tasks

NOTE:
	Python counts the items in a list starting with one, so you shouldn't run into any off-by-one errors when determining the length of a list.
'''
