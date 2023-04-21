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


