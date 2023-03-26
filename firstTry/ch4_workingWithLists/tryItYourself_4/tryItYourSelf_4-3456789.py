# Try It Yourself

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1-20, incluseive.
for numbers in range(1,21):
	print (numbers)
	
# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.  (if tho output is taking too long, stop by pressing Ctrl+C or by closing the output window.)
oneMillionList = []
for income in range(1, 1_001):
	# oneMillionList = income
	oneMillionList.append(income)
	
print(oneMillionList)
print("Too much numbers, being 1 million, so I broke it down to 1,000.")

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.  Also, use the sum() function ot see how quickly Python can add a millino numbers.
print()
minimum_mil = min(oneMillionList)
print(minimum_mil)

print()
maximum_mil = max(oneMillionList)
print(maximum_mil)

print()
total_mil = sum(oneMillionList)
print(total_mil)



print()
# 4-6. Odd Numbers: Use the third argument of the range() funciton to make a list of the odd numbers from 1 to 20.  Use a for loop to print each number. 
odd_numbers = []
for value in range(1, 20, 2):
	print(value)



print()
#4-7. Threes: Make a list of the multiples of 3 from 3 to 30.  Use a for loop to print the numbers in your list.  
lo_threes = []
for value in range(3, 31, 3):
	print(value)



print()
# 4-8. Cubes: A number raised to the third power is called a cube.  For example the cube of 2 is written as 2**3  in Python.  Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the volue of each cube. 
lo_cubes = []
for value in range(1, 11):
	lo_cubes.append(value**2)
print(lo_cubes)




print()
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes
low_cubes = [value**2 for value in range(1,11)]
print(low_cubes)
