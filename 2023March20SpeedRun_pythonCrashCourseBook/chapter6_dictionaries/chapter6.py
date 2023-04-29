# A Simple Dictionary

# alien.py

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])



# Working with Dictionaries (keyValue Pairs)

# Accessing Values in a Dictionary
new_points = alien_0['points']
print(f"You just earned {new_points} points!")


print()
# Adding New Key-Value Pairs
print(alien_0)


print()
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print()
# Starting with an Empty Dictionary
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)




# Modifying Values in a Dictionary
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


# track the Position of an alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position in the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


print()
print(alien_0)
# changing of value in dictionary (changes the whole behavior)
alien_0['speed'] = 'fast'

print(alien_0)





# Removing Key-Value Pairs
# alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)


del alien_0['points']
print(alien_0)



# A Dictionary of Similar Objects
# favorite_languages.py 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


# global variable = local object ???
# add additional working to that new variable for clarity
language = favorite_languages['sarah'].title()
print(f"Sarahs' favorite language is {language}.")



 
# Using get() to Access Values

# continue page 98 and off to Chapter 7

# alien_no_points.py
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
# above print gives KeyError: 'points'

'''
the "get()" method 
- requires a key fo the first arguement
- as a second optional argument, you can pass the value to be returned if the key doesn't exist
'''
# point_value = alien_0.get('points', 'No point value assigned.')

point_value = alien_0.get('points')
print(point_value)



'''
Try it Yourself
6-1. Person:

6-2. Favorite Numbers:

6-3. Glossary:


'''

############################################
############################################
############################################
############################################


# Looping Through a Dictionary
# Looping Through all Key-Value Pairs

# a new dictionary designed to store info about a user on a website

# user.py
user_0 = {
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")    
    print(f"Value: {value}")



print()

# favorite_langauges.py
# see line 93 or search favorite_languages = { 
    # - decided to copy and past it
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# create names for the two variables that will hold the key and value in each key-value pair
# the second half returns the key/value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


print()
###################################

# Looping Through All Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())


# Looping through Keys is actually the default, so 
# for name in favorite_languages:
#
# use the .keys() method to make code easier to read


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")



print()
# Looping Through a Dictionary's Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")





print()
# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())




print()
# Looping Through All Values in a Dictionary
# use set() to pull out the unique duplicate items (nonRepetative)
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())



"""
Try it Yourself
6-4. Glossary 2:

6-5. Rivers:

6-6. Polling:

"""


############################################################

print()
# Nesting

# A List of Dictionaries
# aliens.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}


aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)



############################################################

print()
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens. A series of numbers in range()
# amount of times the loop to repeat
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # append each new alien to the list aliens
    aliens.append(new_alien)

# change first three aliens colors, move faster, and higher points
# as the game progresses
for alien in aliens[:3]:
    # if alien color is green, change color, speed, and points
    if alien['color'] == "green":
        alien['color'] = 'yellow'
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien["speed"] = "fast"
        alien["points"] = 15



# Show the first 5 aliens, using slice
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created (the 30 in the range()).
print(f"Total number of aliens: {len(aliens)}")



print()
############################################################

# A List in a Dictionary
# pizza.py

# Store Information about a pizza being ordered.
pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)



print()
############################################################

# favorite_languages.py
favorite_languages = {
    'jen': ['python', 'ruby'], 
    'sarah': ['c'],
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")




print()
############################################################

# A Dictinary in a Dictionary
# many_users.py

users = {
    'aeinstien': {
        'first': 'albert', 
        'last': 'einstien',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


"""
Try it Yourself
6-7. People:

6-8. Pets:

6-9. Favorite Places:

6-10. Favorite Numbers:

6-11. Cities:

6-12. Extensions:

"""




