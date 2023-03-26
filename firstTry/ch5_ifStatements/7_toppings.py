# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
	
print("\nFinished making your pizza!")




'''
This code would not work properly if we use an if-elif-else block,
because the code would stop running aafter only one test passed 
'''
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
	
print("\nFinished making your pizza!")



'''
NOTE:
	- If you want only one block of code to run, use an if-elif-else chain
	- If more than one block of code needs to run, use a series of independent if statements
'''
