# Try it Yourself
'''
4-13. Buffet: A buffet-style restaurant offers only live basic foods.  Think of five (or in my case, more) simple foods, and store them in a tuple.

- a. Use a for loop to print each food the restaurant offers.
- b. Try to modify one of the items, and make sure that Python rejects the change. 
- c. The restaurant changes its menu, replacing two of the itmes with different foods.  And a line that rewerites the tuple, and then use a for loop to print each of the items on the revised menu.
'''

buffet_foods = ('salad', 'yellow plantain', 'broccoli', 'apple', 'orange', 'plum', 'trailmix', 'goji berry')
# a 
for food in buffet_foods:
	print(food)
	
# b
# buffet_foods[2] = 'spinach'

# c
print()
	buffet_foods = ('salad', 'yellow plantain', 'broccoli', 'spinach', 'veggie crackers', 'apple', 'orange', 'plum', 'trailmix', 'goji berry')
for food in buffet_foods:
	print(food)
	


