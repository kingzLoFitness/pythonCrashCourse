cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
	


'''
Conditional Testing
'''
car = 'bmw'
print(car == 'bmw')


print()
car = 'audi'
print(car == 'bmw')


print()
'''
Ignoring Case when Checking for Equality

'''
car = 'Audi'
print(car == 'audi')


print(car.lower() == 'audi')

print(car)
