'''
# a simple Dictionary...  am i able to write on iPad Pro 10.5 in pretty fast without my external keyboard?
- effectively they can model real-world situations

game featuring aliens with different colors and point values as stored information 
'''
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print()
print(alien_0)





print()
'''
# Working with Dictionaries
- a collection of key-value pairs 
- each key is connected to a value
- and you can use a key to access the value associated with that key

- you can use any object as a value in a dictionary


# accessing value in a dictionary

'''
new_points = alien_0['points']
print(f"You just entered {new_points} points!")

print()
# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print("\n")
# Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)




print("\n")
# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"This alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")





print('\n')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3
	
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")




print("\n")
# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
