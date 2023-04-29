# Using a while Loop with Lists and Dictionaries

# Moving Items from One List to Another

# confirmed_users.py

# Start with users that need to be verified, 
# and an empty list to hold cofirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

'''
# Verify each user until there ar no more unconfirmed users.
# Move each verified user into the list of confirmed users.'''
while unconfirmed_users:
    '''# the pop() function removes unverified users one at a time from the end of unconfirmed_user, removed, assigned to current_user, '''
    current_user = unconfirmed_users.pop()

    ''' 
    - Print the assigned to current_user, 
    - and added to the confirmed_users list (last in (Candace), first out, then Brian and Alice) '''
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print()
########################################################
# Removing All instances of Specific Values from a List
# pets.py

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)



########################################################

# Filling a Dictionary with User Input
# mountain_poll.py

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb today? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete.  Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} wouild like to climb {response}.")




'''
Try it Yourself
7-8. Deli:

7-9. No Pastrami:

7-10. Dream Vacation:


'''

