#Try It Yourself
'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza.  Store these pizza names in a list, and then use a for loop to print the name of each pizza.  
- Modify your for loop to print a sentence usiing the name of the pizza instead of printing just the name of the pizza.  For each pizza you should have one line of output containing a simple statement like "I like pepperoni pizza."
- Add a line at the end of your program, outside the for loop, that states how much you like pizza.  The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''
favPizza = ['Vegetable Pizza', 'Chicken Pizza', 'Multi Cheese Pizza']

# print the name of each pizza
for pizza in favPizza: 
	print(pizza)

	# modify to print a asentence using the name of the pizza
	print(f"I like {pizza}.")
	
# outside of loop.  3 or more lines abotu the kinds of pizza liked 
print(f"\nI prefer {favPizza[0]} over {favPizza[1]} and {favPizza[2]}, \ndue to being more mindful over the foods I eat nowadays.")
# additional sentence
print("I used to really love pizza.")


print("\n")
'''
4-2. Animals: Think of at least three different animals that have a common characteristic.  Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
- Modify your program to print a statement about each animal, such as A dog would make a great pet.  
- Add a line at the end of your program stating what these animals have in common.  You could print a sentense such as Any of these animals would make a great pet!
'''

# at least 3 animals with Common Characteristics
predatorAnimal = ['lion', 'Cheetah', 'Panther']

# for loop and print 
for predator in predatorAnimal:
	print(predator)
	# modified statement about each animal
	print(f"A {predator} would not make a gerat pet.")
	
# what does these animals have in common.   
print("\nNone of these animals would make a great pet.")
