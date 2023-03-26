# How the input() Function Works
message = input("Tell me something, and I will repeat it back to you: ");
print (message);

# Writing Clear Prompts
# greeter.py
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")


#Using int() to Accpt Numerical Input
age = input("How old are you? ")
print(f"Thank you for your age of {age}.  Your welcome.")

# rollercoster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else: 
    print("\nYou'll be able to ride when you're a little older.")


# The Modulo Operator
# even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

