'''
Copying a List
- to start with an existing list and make an entirely new list based on the first one
- make a slice that includes the entire original list by omitting the first index and the second index ([:])
- starts at the first and ends with the last item, producing a copy of the entire list
'''
# list of favorite foods and separate list of foods taht a friend likes (everything in list so far)
my_foods = ['pizza', 'falafel', 'carrot cake']
# create new list. thier list by copying ours
friend_foods = my_foods[:]

# when printed, both contains the same foods
print("- My favorite foods are:")
print(my_foods)


print("\n- My friends's favorite foods are:")
print(friend_foods)


print("-------------------")
'''
- to prove 2 separate lists, add new food to each list and
- show that each list keeps track of the appropriate person's favorte foods:
'''
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("- My favorite foods are:")
print(my_foods)

print("\n- My friends favorite foods are:")
print(friend_foods)


print("-------------------")
# this doesn't work
# does not produce 2 sepaarte lists 
# this is copying a list  without a slice 
# instead of storing a copy, both  variables point to the same list
friend_foods = my_foods

# when food is added (append) this time it will appear on both lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

# output now shows that both are the same now, what we didn't want
print("- My favorite foods are:")
print(my_foods)

print("\n- My friends favorite foods are:")
print(friend_foods)




'''
NOTE: 
	Make sure youa re copying the list using a slice 
'''
