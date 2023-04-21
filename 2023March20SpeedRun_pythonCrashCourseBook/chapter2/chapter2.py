print("Hello Python world!")

message = "Hello Python World!"
print(message)


# Variables 
message = "Hello PYthon Crash Course World!"
print(message)

# Naming and Using Variables

# Variables are Labels

# Try it Yourself 
# 2-1 Simple Message
messageVar = "This is kingzLoFitness!"
print (messageVar)

# 2-2. Simple Messages:
messageVar2 = "This is kingzLoFitness stating another message."
print (messageVar2)

messageVar2 = "This is kingzLoFitness stating another message that overrides last message by assigning another value to the same variable."
print (messageVar2)



# Strings
print("This is a string.")

print("This is also a string.")



# Changing Case in a String with Methods
#name.py 
name = "kingsley cross"
print(name.title())



name = "Kingsley Cross"
print(name.upper())
print(name.lower())


# using Variables in Strings
# full_name.py
first_name = "kingsley"
last_name = "cross"
full_name = f"{first_name} {last_name}"
print(full_name)



print(f"Hello, {full_name.title()}!")





# note: 3.5 or earlier format() method rather than the f syntax
'''
full_name = "{} {}".format(first_name, last_name)
'''

# Adding Whitespace to Strings with Tabs or Newlines
print("Python")


print("Languages:\nPython\nC\nJavaScript")


# Stripping Whitespace

favorite_language = 'python '
print(f"{favorite_language}with space.")

print(f"{favorite_language.rstrip()}without space.")


whiteSpaceSample = " whitespace "
print(f"Sample of {whiteSpaceSample} in sentance.")


print(f"Sample of {whiteSpaceSample.rstrip()} in sentance (rstrip).")

print(f"Sample of {whiteSpaceSample.lstrip()} in sentance (lstrip).")

print(f"Sample of {whiteSpaceSample.strip()} in sentance (strip).")



# Avoiding Syntax Errors with Strings
# apastrophe.py
message = "One of Python's strengths is its diverse community."
print(message)


'''
message = 'One of Python's strengths is its diverse community.'

ouput: SyntaxError: invalid syntax
'''

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Try it Yourself page 25
# 2-3 Personal Message 
# 2-4 Name Cases: 
# 2-5 Famous Quote
# 2-6 Famous Quote2
# 2-7 Stripping 


# Numbers

# Integers  
print(2+3)
print(3**4)

print((2+3) * 4)

print(10** 6)



# Floats
print(0.1 + 0.1)

print(3*00.1)

print(0.2 + 0.1)



# Integers and Floats
print(4 / 2)

print(1 + 2)
print(3.0 ** 2)


# Underscores in Numbers

universe_age = 14_000_000_000
print(universe_age)



# Multiple Assignment
x, y, z = 0, 1, 2
print(y)
print(z)



# Constants
MAX_CONNECTOINS = 5000


'''
Try it Yourself page 28
2-8. Number Eight

2-9. Favorite Number


'''




# Comments
# comment.py
# Say hell to everyone
print("Hello Python people!")



# What Kind of Comments Should You Write?



"""
Try it Yourself
2-10. Adding Comments
"""

# The Zen of Python 

"""
Try it Yourself 
2-11. Enter - import this - into a Python terminal sessions


Output:
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""




