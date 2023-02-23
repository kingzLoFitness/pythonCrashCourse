fname = "kingsley"
lname = "cross"

print(fname + " " + lname)


fullName = fname + " " + lname
print(fullName.upper())

'''
# Place the leter f immediately before the opening quoteation mark.  inserts a variable's value into a string,
putting braces around the name or names of any variable you want to use inside the string
Python will replace each variable with its value when the string is displayed

these strings are called f-strings
the f is for format - Python formats the string by replacing the name of any variable in braces with its value
'''
fullName2 = f"{fname} {lname}"
print(fullName2)

print(f"Hello, {fullName2.title()}")



# this is the same as above, but assigning the message to the variable
# making the final print call simpler
message = f"Hello, {fullName2.title()}!"
print(message)


'''
NOTE: 

F-Strings were first introduced in Python 3.6.

If your using Pyton 3.5 or earlier 
you'll need to use the format() method rather than this f syntax.  
list the variables you want to use in the string inside the parenthesis following format
Each variable is referred to by a set of braces; 
the braces will be filled by the values listed in parentheses in the order provided:
'''
fullName = "{} {}".format(fname, lname)
print(fullName + "your being tested in a sense.  Imagine that.")




print()
print()
print()


#print("Adding Whitespace to Strings with Tab or Newlines")
print("Adding Whitespace to Strings with Tab or Newlines")
print("Python")
print("\tPython")


print("languages:\n\tPython\n\tC\n\tJavaScript")



print()
print()
print()

'''
# Stripping Whitespace.
# NOTE this should actually be executed via the CONSOLE to see it in action 

favorite_language = 'python '
favorite_language 

favorite_language.rstrip()
favorite_language 
'''	

message = "One of Python's strengths is its diverse community."
print(message)



universe_age = 14_000_000_000
print(universe_age)



# Say hello to everyone.
print("Hello Python people!")
