# Try it Yourself

'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
	- Print the message: The first three items in the list are: Then use a slice ot print the first three items from that program's list.
	- Print the message: Three Items fromt he middle of the list are: USe a slice to print three items from the middle of the list.
	- Print the message: The last three items in the list are: Use a slice to print the last three items in the list.
'''
players = ['charles', 'martina', 'michael', 'floerence', 'eli']
# print message of first three items
print("The first three items in the list are: ")
# use a slice to print the first three items from that program's list
for player in players[:3]:
	print(player.title())


print()
# print the message
print("Three items from the middle of the list are:")
# use a slice tool to 3 items from the middle of the list
for player in players[1:4]:
	print(player.title())
	
	
print()
print("The last three items in the list are:")
for player in players[-3:]:
	print(player.title())


print()
'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercies 4-1 (page 56).  Make a copy of the list of pizzas, and call it friend_pizzas.  Then, do the following:
	- Add a new pizza to the original list.
	- Add a different pizza to the list of friend_pizzas.  
	- Prove that you have two separate lists.  Print the message: My favorite pizzas are:, and then use a for loop to print the first list.  Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list.  Make sure each new pizza is stored in the appropriate list.
'''

# program 4-1 Exercise
favPizza = ['Vegetable Pizza', 'Chicken Pizza', 'Multi Cheese Pizza']
friend_pizzas = favPizza[:]

favPizza.append('Anchovies')
friend_pizzas.append('Pepporoni')

print('My favorite pizzas are:')
for pizza in favPizza[:]: 
	print(pizza)
	
print()
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas[:]:
	print(pizza)
	





print()
'''
4-12. More Loops: All versions of foods.py in this section have avoided using the for loops when printing to save space.  Chose a version of foods.py and write two for loops to print each list of foods.
'''
my_foods = ['pizza', 'flafel', 'carrot cake']

print("Here is the list of my foods:")
for food in my_foods[:]:
	print(food)
	
print()
print("But my favorit are 2, the last 2.  Here they are:")	
for food in my_foods[-2:]:
	print(food)
	

print()
my_foods.append('veggie crackers')
my_foods.append('rum cake') 
my_foods.append('ginger cookies')
my_foods.append('bananas')
my_foods.append('apples')
my_foods.append('orange') 
my_foods.append('plumb')
print(my_foods)

for food in my_foods[1:-1:2]:
	print(food)
