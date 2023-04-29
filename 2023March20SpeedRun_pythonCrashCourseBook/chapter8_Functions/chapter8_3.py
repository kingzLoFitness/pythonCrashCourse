# Return Values

# Returning a Single Value

# formatted_name.py
def get_formatted_name(first_name, last_name):
    """Return an full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)



###############################################

# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)



print("\n\nWhere middle name is optional")
# where middle name is optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"    
    return full_name.title()





musician = get_formatted_name('Jimmy', 'hendrix')
print(musician)


musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



#################################################
# Returning a Dictionary
# person.py

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""

    # takes in a first and last name, and puts these values into a dictionary
    person = {'first': first_name, 'last': last_name}

    # the entire dictinary representing the person is returned
    return person


musician = build_person('jimi', 'hendrix')

# the returned value is printed
print(musician)





###################################################
# 

# special value "None"
# used when a variable has no specific value assigned to it
# think of "None" a placeholder value
# in a conditional test, none equals to False 

# this function always stores a person's name, 
# but it can also be modified to store any other information you want about a person
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)



print()
###################################################
# Using a Function with a while Loop
# greeter.py

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name}, {last_name}"
    return full_name.title()

'''# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")

    f_name = input("First name: ")
    l_name = input("Last name: ")
'''


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break 

    l_name = input("Last name: ")
    if l_name == 'q':
        break


    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")




'''
Try it Yourself
8-6. City Names:

8-7. Album:

8-8. User Albums:

'''