# Try It YourSelf

'''
Try The short short programs to get some firsthand expiernece with Python's lists.  You might want to create a new folder for each chappter's exercise to keep them organized 
'''

'''
3-1 Names: Store the name of friends, infulences or whoever in a list called names.  Print each person's name by accesing each elements in the list, one at time.
'''

names = ['Sevan Bomar', 'Stephen Silver', 'Marva Gordon', 'Marcia Gordon', 'Seriah Cross', 'Ridel Cross', 'Davic', 'Tamika Willimas', 'Wilney']

print(names)

print()
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print(names[7])
print(names[8])



'''
3-2 Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person's name, print a message to them.  The text of each message should be the same, but each message should be personalized with the person's name.
'''
print()
print("3-2 Greetings")
print(names)
print("---------------------------")
print("Hello to the people in my list of names, welcome " + names[0] + '.')
print("Hello to the people in my list of names, welcome " + names[1] + '.')
print("Hello to the people in my list of names, welcome " + names[2] + '.')
print("Hello to the people in my list of names, welcome " + names[3] + '.')
print("Hello to the people in my list of names, welcome " + names[4] + '.')
print("Hello to the people in my list of names, welcome " + names[5] + '.')
print("Hello to the people in my list of names, welcome " + names[6] + '.')
print("Hello to the people in my list of names, welcome " + names[7] + '.')
print("Hello to the people in my list of names, welcome " + names[8] + '.')


print()
print("End of list after putting in 'names[-1]' in the last print statement.")
# print("Hello to the people in my list of names, welcome " + names[9] + '.')
# this last code is beyond the index
# my thoughts is to put in names[]-1 or something like that
# I was close, it's actually names[-1]'
print("Hello to the people in my list of names, welcome " + names[-1] + '.')




'''
3-3 Your Own List: Think of your favorite mode of transportation, such as a motocycle or a car, and make a list that stores several examples.  Use your list to print a series of statements about these items, such as "I would like to own a Honda motocycle."
'''

favModesOfTransport = ['honda', 'skateboard', 'bicycle', 'scooter', 'inlineSkate']

print()
print("This is 3-3 based on my own List of favModesOfTransport (my various forms I used + 1)")
print(favModesOfTransport)
print("--------------------------------")
print("I would like to get a " + favModesOfTransport[0] + " to drive around in for long distances and/or faster way of transport.")

print("\nSince this time of this Pandemic, I've learned to " + favModesOfTransport[1] + " in a sense of conditioning myself at the same time.  Less on use of transportation though.")

print("\nIn the past I've used " + favModesOfTransport[2] + " as a form of transportation going to and fro to different parks.")

print("\nThere was a time I use the " + favModesOfTransport[3] + " to go through travels for miles on end to pick up meds for my Grandmother.")

print("\nMy first form of transportation was " + favModesOfTransport[4] + " to go to the work at Kings Plaza.  Working at the Movie Theater.")
