# Try it YourSelf
'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game.  Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
	- Write an if statement to test whether the alien's color is green.  If it is,print a message that the player just earned 5 points.
	- Write one version of this program that passes the if test and another that fails.  (The version that fails will have no output)
'''
alien_color = 'green'

if alien_color == 'green':
	print("Congrates player, you earned 5 points.")

if alien_color != 'red':
	print("Too bad you didn't get the red version of the Alien.  That would've earned you more points.")
	
if alien_color == 'yellow':
	print("Wow, you just earned even more points for hitting up the yellow side of the Alien.")
	
	
	

print()
'''
5-4. Alien Color #2: Choose a color for an alien as you did in Exercies 5-3, and write an if-else chain.
	- If the alien's color is green, print a statement that the player just earned 5 pints for shooting the alien.
	- if the alien color isn't green, print a statement that the player just eaerned 10 points.
	- Write the version of this program that runs the if block and another that runs the else block.
'''
alien_color = 'red'

if alien_color == 'green':
	print("Congrate player, you earned 5 points for shooting the alien.")
else:
	print("You just earned 10 poaints on that red color shot of the alien.")
	

print()
alien_color = 'green'

if alien_color == 'green':
	print("Congrates player, you earned 5 points for shooting the alien.")
else:
	print("You just earned 10 poaints on that red color shot of the alien.")
	

	


'''
5-5. Alien Color #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
	- If the alien is green, print a message that the player earned 5 points.
	- If the alien is yellow, print a message that the player earened 10 points.
	- If the alien is red, print a message that the player earned 15 points.
	- Write three version of this program, making sure each message is printed for the apppropriate color alien.
'''
print()
alien_color = 'red'

if alien_color == 'green':
	print("Congrate player, you earned 5 points for shooting the alien.")
elif alien_color == 'yellow':
	print("You just earned 10 poaints on that red color shot of the alien.")
elif alien_color == 'red':
	print('Hey Player, you just earned a whopping 15 pints.')

print()
alien_color = 'yellow'

if alien_color == 'green':
	print("Congrate player, you earned 5 points for shooting the alien.")
elif alien_color == 'yellow':
	print("You just earned 10 poaints on that yellow color shot of the alien.")
elif alien_color == 'red':
	print('Hey Player, you just earned a whopping 15 pints.')


print()
alien_color = 'green'

if alien_color == 'green':
	print("Congrate player, you earned 5 points for shooting the alien that was green.")
elif alien_color == 'yellow':
	print("You just earned 10 poaints on that yellow color shot of the alien.")
elif alien_color == 'red':
	print('Hey Player, you just earned a whopping 15 pints on that red alien.')

	


print()
'''
5-6. Stage of Life: Write an if-elif-else chain that determins a person's stage of life.  Set a value for the variable age, and then:
	- If the person is less than 2 years old, print a message that the person is a baby.
	- If the person is at least 2 years old but less than 4, print a message that the peson is a toddler.
	- If the person is at least 4 years old but less than 13, print a message that the person is a kid.
	- If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
	- If the person is at least 20 years old but less than 65, print a message that the person is an adult. 
	- If the person is age 65 or older, print a message that the person is an elder. 
'''
age = 42

if age < 2:
	print("Awe, your just a baby.")
elif age >= 2 and age < 4:
	print("Hey little toddler.")
elif age >= 4 and age < 13:
	print("Hello, I see your the age of a kid.")
elif age >= 13 and age < 20:
	print("Hey, I see your a teenager.")
elif age >= 20 and age < 65:
	print("Hey person, I see your at adult age.")
elif age >= 65:
	print("Welcome, elder.")


print()
'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
	- Make a list of your three favorite fruits, and call it favorite_fruits
	- Write five if statements. Each should check whether a certain kind of fruit is in your list.  If the fruit is in your list, the if block should print a statement, such as You really like bananas!
'''
favorite_fruit = ['apple', 'orange', 'plum']

if 'apple' in favorite_fruit:
	print("Wow, your favorite fruit is apple.")
	
if 'orange' in favorite_fruit:
	print("Wow, your favorite fruit is orange.")
	
if 'plum' in favorite_fruit:
	print("Wow, your favorite fruit is plum.")
	
if 'pear' in favorite_fruit:
	print("Wow, your favorite fruit is pear.")
	
if 'mango' in favorite_fruit:
	print("Wow, your favorite fruit is mango®.")
	

