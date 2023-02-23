'''
Looping Through an Entire List
- repeetative list length
- print out each item on the list
'''
magicians = ['alice', 'david', 'carolina']

# pull names from original list magicians and assiciate it into variable magician
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	# doing more work within a for Loop
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
	
	
# Doing Something After a for Loop
print("Thank you, everyone.  That was a great magic show!")
