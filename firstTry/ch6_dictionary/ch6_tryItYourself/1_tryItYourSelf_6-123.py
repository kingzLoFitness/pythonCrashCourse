# Try It Yourself
'''
6-1. Person: Use a dictionary to store information about a person you know.  Store thier first name, last name, age, and the city in which they live.  You should ahve keys suck as first_name, last_name, age, and city.  Print each piece of information stored in your dictionary.
'''
person = {
	'first_name': 'Seriah',
	'last_name': 'Cross',
	'age': 11,
	'city': 'Brooklyn'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])



print("\n")
'''
6-2. Favorite Numbers: Use a dictionary to share people's favorite numbers.  Think of five names, and use them as keys in your dictionary.  Think of a favorite number for each person, and store each as a value in your dictionary.  Print each person's name and thier favorite number.  For even more fun, poll a few friends and get some actual data for your program.  
'''
favorite_numbers = {
	'kingzlofitness': 7,
	'seriah': 12,
	'tati': 3,
	'betty': 5,
	'veronica': 10
}
print(favorite_numbers)

print("\n")



for name, number in favorite_numbers.items():
	print(f"{name.title()}... favorite number: {number}")
		  



'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.  However, to avoid confusion, let's call it a glossary.
	- Think of five programming words you've learned about in the previous chapters.  Use these words as the keys in your glossary, and store thier meanings as values.
	- Print each word and its meaning as neatly formatted output.  You might print the word followed by a colon and then its meaning indented on a second line.  Use the newline character (\n) to insert a blank line between each word-meaning prior in your output.
'''

glossary = {
	
}










