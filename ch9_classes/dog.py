# define a class named Dog / Capitalized names refer to classes in Python
class Dog:
    """ A simple attempt to model a dog. """  # a docstring defining what this class does

    # a functon that is part of a class is called a method
    # everythoing about functions applies to methonds as well
    # only practical difference for now os the way we'll call methods
    def __init__(self, name, age):
        """ Initialize name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


"""
********************************************************************
Making an Instance from a Class
- a class is a set of instructions for how to make an instance
- th class Dog os a set of instructions that tell Python how to make individual instances represento9ng specific dogsl
"""
my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


"""
********************************************************************
Calling Methods
- to call a method, give the name of the instance (in this case my_dog) and the metod yu want to call, separated by a dot
- when Python reads my_dog.sit, it looks for the method sit() in the class Dog and runs that code
- same for my_dpg.roll_over()
"""
my_dog.sit()
my_dog.roll_over()


"""
********************************************************************
Creating Multiple Instances
- you can ceate as many instances from a class as you need 
    - with its own set of attributes, capable of the same set of actions
- even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class

- create a second dog called your_dog
"""
your_dog = Dog("Lucy", 3)

print(f"\nYOur dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
