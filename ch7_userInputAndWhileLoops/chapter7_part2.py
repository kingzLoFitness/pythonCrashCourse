# Introducing while Loops

# counting.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("End of while loop")


# Letting the User Choose When to Quit
# parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)






# Using a Flag

prompt = "\nTell me someting, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# this flag, we'll call active (or anything), will monitor whether or not the program should continue running:
'''
set the variable active to true so the program starts in an active state
- doing so makes the while statement sipler because no comparison is made in the while statement itself;
the logic is taken care of in other parts of the program.
- as long as the active variable remains True, the loop will continue running.
'''
active = True

while active:
    message = input(prompt)

    '''
    in the if statement inside the while loop, we check the value of message once the user enters thier input. 
    - if the user enters 'quit', we set active to false and the while loop stops
    - if the user enters anything other than 'quit', we print their input as a message
    '''
    if message == 'quit':
        active = False
    else:
        print(message)

    




# Using break to Exit a Loop

# cities.py

prompt = "\nPleanse enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

'''
a loop that starts with while True will run forever unless it reaaches a break statement 
- the loop in this program continues asking the user to enter the names of cities they've been to until they enter 'quit'.  
- when they enter 'quit', the break statement runs, causing Pythin to exit the loop.
'''
while True:
    city = input(prompt)

    if city == 'quit':
        # causes Python to break    
        break
    else:
        print(f"I'd love to go to {city.title()}!")



