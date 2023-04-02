# Defining a Function

# greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello")

greet_user()



#######################

# Passing Information to a Function

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('kingsley')


#######################

# Arguments and Parameters


#############################

# Passing Arguments

# Positional Arguments

# pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""