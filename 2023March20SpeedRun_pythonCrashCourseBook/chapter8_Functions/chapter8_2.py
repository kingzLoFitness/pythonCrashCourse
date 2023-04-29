# Arguments and Parameters

# Passing Arguments

# Positional Arguments

# pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')




######################################

# Multiple Function Calls

describe_pet('dog', 'willie')




print("\n")
######################################
# Order Matters in Positional Arguments
print("# Order Matters in Positional Arguments")
describe_pet('harry', 'hamster')



######################################
# Keyword Arguments
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# the order of keyword arguments doesn't matter because Python knows where each value should go
describe_pet(pet_name =  'harry', animal_type = 'hamster')


# NOTE: when you use "keyword" arguments, be sure to use the exact names of the parameters in the functions's definition




######################################
# Default Values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a(n) {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='harry')

describe_pet('harry')


'''# to describe an animal type other than a dog
# because an explicit argument for animal_type is provided, Python will ignore the parameter's default value'''
describe_pet(pet_name='harry', animal_type='hamster')



'''NOTE: when you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values
- this allows Python to continue interpreting positional arguments correctly'''




######################################
# Equivalent Function Calls


"""
NOTE: It doesn't really matter which calling style you use.
-  as long as your function calls produce the ouput you want, 
- just use the style you find easiest to understand.
- (based on examples given above)
"""



######################################
# Avoiding Argument Errors

''' 
example (I had to comment this out)

describe_pet()

TypeError: describe_pet() missing 1 required positinal argument: 'pet_name'
'''


"""
Try it Yourself
8-3. T-Shirt:

8-4. Lorge Shirts:

8-5. Cities:
    
"""