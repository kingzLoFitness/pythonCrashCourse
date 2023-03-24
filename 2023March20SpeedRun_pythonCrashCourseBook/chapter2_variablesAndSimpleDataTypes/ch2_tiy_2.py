"""
Try It Yourself
Save each of the following exercises as a separate file with a name like
name_cases.py. If you get stuck, take a break or see the suggestions in
Appendix C.
"""

"""
2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
"""
personName = "Seriah"
print(f"Hello {personName}, would you like to learn some Python today?")

"""
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
"""
print(personName.lower())
print(personName.upper())
print(personName.title())

"""
2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
"""
famousArtist = "Hamlet"
famousQuote = '"To be or not to be, that is the Question"'

print(f"{famousArtist} quoted (or once stated) {famousQuote}")

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
famous person’s name using a variable called famous_person. Then compose
your ­message and represent it with a new variable called message. Print your
message.
"""

famous_person = famousArtist
print()
print(f"{famous_person} again, quoted (and/or once stated) {famousQuote}")




"""
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip()
"""


