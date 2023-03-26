# Try it Yourself
'''
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.  Imagine you are writing code that will print a greeting to each user after they log in to a website.  Loop through the list, and print a greetin to each user:
	- If the username is 'admin' (kingzlofitness), print a special greeting, such as Hello admin, would you like to see a status report?
	- Otherwise, print a generic greeting, suck as Hello Jaden, thank you for loggin in again.
'''
usernames = ['racketink', 'snydah','kingzlofitness', 'kingzlo', 'errol']

for user in usernames:
	if user == 'kingzlofitness':
 		print("\nSee about caps anywhere in kingzlofitness.")
 		print("Another concept A & I, being both letter and word.\n")
	print(f"Welcome, {user.title()}!")
	


print()
print("This is 5-9 Example\n-------------------\n")
'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
	- If the list is empty, print the message We need to find some users!
	- Remove all of the usernames from your list, and make sure the correct message is printed.
'''
# hello_admin.py (file)
usernames2 = []
if usernames2:
	for username in usernames2:
		print(f"WAelcome, {username.title()}!")
else:
	print("We need to find some users!")





print()
print("This is 5-10 Example\n--------------------")
'''
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
	- Make a list of five or more usernames called current_users.
	- make another list of five usernames called new_users.  Make sure one or two of the new usernames are also in the current_user list.
	- Loop through the new_users list to see if each new username has already been used.  If it has, print a message that the person will need to enter a new username.  If a username has not been used, print a message saying that the username is available.
	- Make sure your comparison is case insensitive.  If 'John' has been used 'JOHN' should not be accepted.  (To do this, you'll need to make a copy of current_users containing the lowercase versions of all existing users.)
'''
current_users = ['kingzlofitness', 'harryPotter', 'EricThomas', 'SevanBomar', 'JackieChan']
new_users = ['kingzlofitness', 'ShantelCox', 'RichardPrior', 'JackieChan', 'NanciDrew', 'KINGZLOFITNESS', 'kingzlofitness']

for users in new_users:
	if users in current_users:
		print(f"Username, {users}, has already been used.  You will have to enter a new user.")
	elif users.lower() in current_users:
		print(f"USERNAME, {users}, has already been used.  You will have to enter a new user.")
	else:
		print(f"Username, {users}, is available.")




print()
'''
5-11. Ordinary Numbers: Ordinal numbers indicate thier position in a list, such as 1st or 2nd.  Most ordinal numbers end in th, except 1, 2, and 3.
	- Store the numbers 1 through 9 in a list.
	- Loop thorugh the list.
	- Use an if-elif-else chain inside the loop to print the proper original ending for each number.  Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result shoudl be on a separate line.
'''
ord_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in ord_numbers:
	if num == 1:
		print(f"{num}st")
	elif num == 2:
		print(f"{num}nd")
	elif num == 3:
		print(f"{num}rd")
	else:
		print(f"{num}th")
	




