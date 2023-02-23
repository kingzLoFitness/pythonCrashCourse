'''
Working with Part of a List
- how to work with all the elements in a list
- you can also work with a specific group of items i a list 
- Python calls it a slice

Slicing a List
- to make a slice, you specify the index.of the first and last elements you want to work with
- as with the range() function, Python stops one item before the second index you specify.
- EXAMPLE: to index the first three elements in a list, you would request indices 0 through 3
		- which would return elements 0, 1, and 2.
'''
# a list of players on a team
players = ['charles', 'martina', 'michael', 'florence', 'elil']
print(players[0:3])		# slice the list showing the first three players on the list


print()
print(players[1:4])		# subset of a list; 2nd, 3rd, and 4th items on the list

print()
# omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])		

print()
# simlilar syntax if you want a slice that includes the end of a list
# all items from the third through the last items
print(players[2:])

print()
# recall that a negative index returns an element a certain distance from the end of a list.
# to output the last 3 players
print(players[-3:])




'''
Looping Through a Slice
- you can use a slice in a for loop of you want to loop through a sublet of the elements in a list.
'''
print()
print("Here are the first three players on my team:")
# loop through the first three players and print their names as part of a single roster
for player in players[:3]:
	print(player.title())
	
	

'''
- slices are useful in a number of situations
- EXAMPLE(s)

- you could add a player's final score to a list every t ime that player findishes playing.
- you could then get a player's top three scores by sorting the list in decreasing order and taking a slice that includes just ther first three scores

- when your woerking with data, you can use slices to process your data in chunks of a specific size.  

- or when your building a web application, you could use slices to display information in a series of pages with an appropraite amount of information on each page.  
'''
