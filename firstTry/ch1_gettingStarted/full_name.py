first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name}{last_name}'
print(full_name)
print()
print(f"Hello, {full_name.title()}!")



# to insert a variable's value into a string, place the letter f immediately before the opening quotatoin mark.  
# put braces around the name or names of any variable you want to tuse inside the string
# python will replace each variable with its value when the string is displayed

# these strings are called f-strings
# the f is for format, because Python formats the string by replacing the name of any variable in braces with its value

print()
print("Python")
# tab space before printout
print("\tPython")

print()
# new line and tab spaces of each language
print("Languages:\n\tPython\n\tC\n\tJavaScript")


# ------------------------------------------------------
# This is made more for the console to print out directly 
# so more to print out via Console
print()
favorite_language = 'hello python world'
print(favorite_language)

print("This is dealing with '.rstrip'")
favorite_language = favorite_language.rstrip()
print(favorite_language)

# -----END .rstrip example





print('\n\n\n\n')
# ------------------------------------------------------
# Try it Yourself
print('\t\t\t# Try it Yourself')

'''
2-3 Personal Message
Use a variable to represent a person's name, and print a message to that person.  Your message  should be simple, such as "Hello KINGZLOfitnes, would you like to learn some Python today."
'''
userName = "KINGZLOfitness"
print("Hello " + userName + ", would you like to laern some Python today?")




'''
2-4 Name Cases: Use a variable to represent a person's name, and and then print that person's name in lowercase, uppercase, and title case.
'''
print(userName.lower())
print(userName.upper())
print(userName.title())
