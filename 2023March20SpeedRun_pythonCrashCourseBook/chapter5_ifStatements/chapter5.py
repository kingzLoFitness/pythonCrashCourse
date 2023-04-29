# if statements

# A Simple Example
# cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())


print()
# Conditional Tests
# Checking for Equality
car = 'bmw'
print(car == 'bmw')


car = 'audi'
print(car == 'bmw')



# Ignoring Case when Checking for Equality
car = 'Audi'

print(car == 'audi')
print(car.lower() == 'audi')


print("\n\n")

# Checking for Inequality
# toppings.py
requested_topping = 'mushrooms'
 
if requested_topping != 'anchovies':
    print("Hold the anchovies!")




# Numerical Comparisons
age = 18
print(age == 18)


answer = 17

if answer != 42: 
    print("That is not the correct answer.  Please try again")





age = 19 
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)



print()
# Checking Multiple Conditions
# Using "and" to Check Multiple Conditions

age_0 = 22;
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)


age_1 = 22
print(age_0 >= 21 and age_1 >= 21)



print()
# Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)



print()
# Checking Whether a Value is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)



print()
# Checking Whether a Value is Not in a List
# banned_users.py
banned_users = ['andrew', 'caroina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")





# Boolean Expressions
game_active = True
can_edit = False


"""
Try it Yourself 
5-1. Conditional Tests:
- Something like this:
car  = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict True.")
print(car == 'audi')



5-2. More Conditional Tests:
"""


#######################################################
#######################################################
#######################################################

# if Statements
# Simple if Statments
'''
if conditional_test:
    do something
'''

print()
#voting.py

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("have you registered to vote yet?")
# if-else Statements
else: 
    print("Sorry, you ae too young to vote.")
    print("Please register to vote as soon as you turn 18!")


print()
# The if-elif-else Chain
# example: 
    # Admission for anyone under age 4 is free
    # Admission for anyone between the ages of 4 and 18 is $25
    # Admission for anyone age 18 or older is $40

# amusement_park.py
age  = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("YOur admission cost is $40.")



age = 44
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")



# Using Multiple elif Blocks


age = 44
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: 
    price = 20

print(f"Your admission cost is ${price}.")



# Omitting the "else" Block
age = 44
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: 
    price = 20

print(f"Your admission cost is ${price}.")



print()
# Testing Multiple Conditions
# toppings.py
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")



"""
Try it Yourself page 84
5-3. Alien Colors #1:

5:4. Alien Colors #2:

5-5. Alien Colors #3:

5-6. Stages of Life:

5-7. Favorite Fruit:

"""



#######################################################
#######################################################
#######################################################

# Using if Statements with Lists

# Checking for Special Items
# toppings.py 
print()
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


print()
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("- Sorry, we are out of green peppers right now.")
    else:
        print(f"- Adding {requested_topping}.")
    
print("\nFinished making your pizza!")




# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print()
# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepparoni' 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"- Adding {requested_topping}.")
    else:
        print(f"- Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")



"""
Try it Yourself page 89
5-8. Hello Admin:

5-9. No Users:

5-10. Checking Usernames:

5-11. Ordinal Numbers:

"""




#######################################################
#######################################################
#######################################################

# Styling Your "if" Statements

"""
if age < 4:

is better than:

if age<4:
"""

"""
Try it Yourself page 90
5-12. Styling if statements:

5-13. Your Ideas:
"""




#######################################################
#######################################################
#######################################################










#######################################################
#######################################################
#######################################################












#######################################################
#######################################################
#######################################################
