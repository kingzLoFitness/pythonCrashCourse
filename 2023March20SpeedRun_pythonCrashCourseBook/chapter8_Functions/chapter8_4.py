# Passing a List
# When you pass a list to a function, the function gets direct access to the contents of the list
# using functions to make working with lists more efficient

# a list of users 
# and want to print a greeeting to each

# greet_users.py
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


