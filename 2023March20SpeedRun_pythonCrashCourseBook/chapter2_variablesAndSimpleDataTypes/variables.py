# Variables 

# hello_world.py 

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course reader!"
print(message)


'''
Strings:

"This is a string."
"This is also a string."

'''

# Changing CAse in a String with Methods
# name.py

name = "Kingsley Cross"
print(name.title())
print(name.upper())
print(name.lower())



##########################################


# Using Variables in Strings
# full_name.py

# f-string to compose complete messages using the info assiciated with a variable

first_name = "kingsley"
last_name = "cross"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


message = f"Hello, {full_name.title()}!"
print(message)


"""
Note with F-strings
- first introduced in Python 3.6
- if using Python 3.5 or earlier, you'll need to use the format() method
    - to use format()
    - list the variables you want to use in the string in side the par3entheses following format.
    - each variable is referred to by a set of braces;
    - the braces will be filled by the values listed in praentheses in the order provided:
    __________________________
    full_name = "{} {}".format(first_name, last_name)
    __________________________
"""

# Adding Whitespace to Strings with Tabs or NewLines
print("Python")

# to add a tab
print("\tPython")

print()
# to add newline in a string
print("Languages:\nPython\nC\nJavaScript")



print()
print("Languages:\n\tPython\n\tC\n\tJavaScript")



# Stripping Whitespace
favorite_language = 'python '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language)



print("White sapce is on th left side")
favorite_language = '    python'
print(favorite_language)


print(favorite_language.lstrip())

print(favorite_language.strip())


