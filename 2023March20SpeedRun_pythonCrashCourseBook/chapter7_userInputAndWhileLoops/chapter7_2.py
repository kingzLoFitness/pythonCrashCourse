# Introducing "while" Loops
# The while Loop in Action

#counting.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1





print()


# Letting the User Choose When to Quit
# parrot.py

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# keep track of whatever value the user enters
# defined as an empty string, "", so Python has something to check the first time it reaches the while line
message = ""

while message != 'quit':
    message = input(prompt)
    print(message)


#########################################################
#########################################################
#########################################################
# Using a Flag
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else: 
        print(message)




# Using "break" to Exit a Loop
# cities.py
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")




# Using "continue" in a Loop 
# to return to the beginning of the loop based on the result of the conditional test
# example, a loop that counts from 1 to 10 but prints only the odd numbers in that range
# counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # the continue statement tells Python to ignore the rest of the loop and return to the beginning
        continue
    
    # if the current number is not divisible by 2, the rest of the loop is executed and Python Prints the current number
    print(current_number)



'''
Avoiding Infinite Loops
# couting.py

x = 1 
while x <= 5:
    print(x)
    x += 1


# this loop runs forever!  
# because x will start at 1 but never change
# because the line x += 1 is omited
x = 1
while x <= 5:
    print(x)
'''




'''
Try it Yourself page 123
7-4. Pizza Toppings:

7-5. Movie Tickets:

7-6. Three Exits:

7-7. Infinity:

'''




