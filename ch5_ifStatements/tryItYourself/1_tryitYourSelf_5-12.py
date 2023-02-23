# Try it Yourself
'''
5-1. Conditional Tests: Write a series of conditional test.  Print a statement describing each test and your prediction for the result of each test.  Your code should look something like this:
_______________________________________________
car = 'subaru'
print("Is car == 'subaru'?  I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')
_______________________________________________

- Look closely at your results and make sure you understand why each line evaluates to True of False

- Create at least ten tests.  Have at least five tests evaluate to True and another five tests evaluate to False.
'''
program = 'python'
# first test
print("Does program == 'python'? I perdict True.")
print(program == 'python')

# second test
print("Does program == 'javaScript'?  I predict True.")
print(program == 'javaScript')

# 2nd Truth third test (4 true and 4 false left to create test)
currentTraining = 'GST'
print("Does my current training == 'GST'?  I predict True.")
print(currentTraining == "GST")

# 3rd Truth fourth test 
instrument = 'piano'
print("Does practice instrument == 'piano'?  I konw it's True.")
print(instrument == 'piano')
# 4th Truth fifth test
instrument = 'guitar'


# 5th Truth sixth test
musicApp = 'yousician'
print("Does practice in musicApp == 'yousician'?  This is definately True.")
print(musicApp == 'yousician')

# 2nd False seventh test
myWeightClass = 'lightWeight'
print("Does my weight class == 'heavyWeight'?  This is difinately False.")
print(myWeightClass == 'heavyWeight')

# 3rd False eighth test
musicChoice = 'hipHop'
print("My music choice == 'heavyMetal'?  This is False.")
print(musicChoice == 'heavyMetal')

# 4th False ninth test
kfwsStatus = 'nonDegreeHolder'
print("My status shows I am a degree holder.  This is False.")
print(kfwsStatus == 'degreeHolder')

# 5th False tenth test
retroArch = '32bit'
print("I can run retroArch == 64bit.  This is False within Retroid Pocket 2.")
print(retroArch == '64bit')


'''
5-2.  More Conditional Tests: You don't have to limit the number of test you create. 
- but it seems like there was more than enough to craete
'''
myHair = 'locks'

if myHair != 'bald':
	print("You are clearly not bald.")



videoGames = 'missionImpossible'

if videoGames == 'missionImpossible':
	print(f"So far you went over Mupen64 Plus and came out and went back in to get back to {videoGames}.")
	



womenIWannaLove = ['Shantel', 'Alexis', 'Suzette', 'Rosebie']
womenJustMet = 'Wilney'

if womenJustMet not in womenIWannaLove:
	print(f"{womenJustMet}, are you too young for me?")
	


