'''
The following exercises are a bit more complex tahn those in Chapter 2, but they give you an opportunity to use lists in all of the ways described
'''

'''
3-4. Guest List: If you could invite anyone, living or deciesase, to dinner, who woould you invitet?  Make a list that includes at least three pepole you'd like to invite to dinner.  Then use your list to print a message to each person, inviting them to dinner.
'''
guestList = ['Grandmother', 'Grandfather', 'Grand_Uncle']
print(guestList)
print("Hi " + guestList[0] + ' you are invited to my dinner party I have invisioned from within.')
print("Hi " + guestList[1] + ' you are invited to my dinner party I have invisioned from within.')
print("Hi " + guestList[2] + ' you are invited to my dinner party I have invisioned from within.')


print()
'''
3-5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.  You'll have to think of someone else to invite.
 - Start with your program from Exercise 3-4.  Add a print() call at the end of your program stating the name of the guest who can't make it.
 - Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting. 
 - Print a second set of invitation messages, one for each person who is still in your list.
'''
print("Sorry " + guestList[2] + " that you can't my dinner party.")


print()
# replace one guest for the next 
newGuestOnList = guestList[2] = "AroundTheWayGirl"
print(guestList)

print("Here is a reminder " + guestList[0] + ", once again from within.  You are invited to my dinner party.")
print("Here is a reminder " + guestList[1] + ", once again from within.  You are invited to my dinner party.")
print("Here is a reminder " + guestList[2] + ", once again from within.  You are invited to my dinner party.") 

'''
 3-6. more Guests: You just found a bigger dinner table, so now more space is available.  Think of three more guests to invite to dinner.
 - Start with your program from Exercies 3-4 or Exercise 3-5.  Add a print() call to the end of your program informing people that you found a bigger dinner table.
 - Use insert() to add one new guest to the beginning of your list.
 - Use insert() to add one new guest to the middle of your list.
 - Use append() to add one new guest to the end of your list. 
 - Print a new set of invitation messages, one for each person in your list.
'''
 
print() 
#  - Start with your program from Exercies 3-4 or Exercise 3-5.  Add a print() call to the end of your program informing people that you found a bigger dinner table.
print("Hey " + guestList[0] + " I found a bigger dinner table.  Stand by for more information.")
print("Hey " + guestList[1] + " I found a bigger dinner table.  Stand by for more information.")
print("Hey " + guestList[2] + " I found a bigger dinner table.  Stand by for more information.") 
 
 
print()
#  - Use insert() to add one new guest to the beginning of your list.
print("- Insert() another guest in the beginning of the Original List.")
print("---------------------------------------------------------------")
guestList.insert(0, "Mom")
print(guestList)

print("\n- Insert() another guest in the middle of the New List.")
print("-------------------------------------------------------")
guestList.insert(2, "Aunt")
print(guestList)


print("\n-Append() another guest at the end of the New List.")
print("---------------------------------------------------")
guestList.append("Daughter")
print(guestList)


print("........ADDED GEUSTS ON LIST.............")
addedGuestOnList = guestList

print()
print (addedGuestOnList)


'''
This is part of 3-6 
See 3.9 Dinner Guests:  
	- to print a message indicating the number of people invited to dinner.
'''
print(f">>>>>>>>>>>>>.      So I've invited {len(guestList)} guests to the dinner party.")


print()
#  - Print a new set of invitation messages, one for each person in your list.
print("Hello " + guestList[0] + ", I had to send this invite again for I've invited 3 more guests.")
print("Hello " + guestList[1] + ", I had to send this invite again for I've invited 3 more guests.")
print("Hello " + guestList[2] + ", I had to send this invite again for I've invited 3 more guests.")
print("Hello " + guestList[3] + ", I had to send this invite again for I've invited 3 more guests.")
print("Hello " + guestList[4] + ", I had to send this invite again for I've invited 3 more guests.")
print("Hello " + guestList[5] + ", I had to send this invite again for I've invited 3 more guests.")

 
'''
3-7. Shrinking Guest List: You just found out that your new dinner table wont arrive in time for the dinner, and you have space for only two guests.
- Start with your program from Exercise 3-6.  Add a new line that prints a message saying that you can invite only two poeple for dinner.
- Use pop() to remove guests from your list one at a time until only two names remain in your list.  Each time you pop a name from your list, point a message to that person letting them know you're  sorry you can't invite them to dinner.
- Print a message to each of the two people still on your list, letting them know they're still invited.
- Use del to remove the last two names from your list, so you have an empty list.  Print your list to make sure you actually have an empty. list at the end of your program. 
'''
 
print()
#- Start with your program from Exercise 3-6.  Add a new line that prints a message saying that you can invite only two poeple for dinner.
print("I can only invite 2 people for dinner.  Sorry for the inconvienience.")
 
 
 
'''
print()
print(guestList)
# - Use pop() to remove guests from your list one at a time until only two names remain in your list.  Each time you pop a name from your list, point a message to that person letting them know you're  sorry you can't invite them to dinner.
 
guestList.pop(0)
print(guestList)

guestList.pop(0)
print(guestList)

guestList.pop(0)
print(guestList)

guestList.pop(0)
print(guestList)


'''

print()
print("........ADDED GEUSTS ON LIST.............")

# NOTE: somehow after the various pop() features I tried to reopen "addedGuestOnList" to show the full list, but somehow it didn't compute, 
print(addedGuestOnList)
# - Use pop() to remove guests from your list one at a time until only two names remain in your list.  Each time you pop a name from your list, point a message to that person letting them know you're  sorry you can't invite them to dinner.


removedGuest = guestList.pop(0)
print("Sorry " + removedGuest + ".  I was only abole to invite 2 people on the list.")

print()
print(guestList)



removedGuest = guestList.pop(1)
print("Sorry " + removedGuest + ".  I was only abole to invite 2 people on the list.")

print()
print(guestList)



removedGuest = guestList.pop(2)
print("Sorry " + removedGuest + ".  I was only abole to invite 2 people on the list.")
print(guestList)


# in the output this enpty .pop() could alsao be .pop(2) because what remained is 3 people on the list
print() 
removedGuest = guestList.pop()
print("Sorry " + removedGuest + ".  I was only abole to invite 2 people on the list.")



# - Print a message to each of the two people still on your list, letting them know they're still invited.
print(guestList)





# - Use del to remove the last two names from your list, so you have an empty list.  Print your list to make sure you actually have an empty list at the end of your program.
del guestList[0]
print(guestList)
del guestList[0]
print(guestList)


