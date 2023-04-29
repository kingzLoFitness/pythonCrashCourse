# How the input() Function Works
# parrot.py 
message = input("Tell me something, and I will repeat it back to you: ")

print(message)



# Writing Clear Prompt
# greeter.py
name = input("Please enter your name: ")
print(f"Hello, {name}!")



print()
# greeter.py
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hell, {name}")




print()
# Using int() to Accept Numerical Input
age = input("How old are you? ")
print(f"You entered you are {age} years old.")

age = int(age)

print(age >= 18)




#########################################################
#########################################################
#########################################################



# fast foward from 116 to page 118

# rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


print()
# The Modulo Operator
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)


print()
# even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")




'''
Try it Yourself

7-1. Rental Car:

7-2. Restaurant Seating:

7-3. Multiples of Ten:

'''
#########################################################
#########################################################
#########################################################





