# The __init__() function is called automatically
# every time the class is being used to create a new object.
# To understand the meaning of classes we have to understand the built-in __init__() function.
#
# All classes have a function called __init__(), which is always executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties, or other operations
# that are necessary to do when the object is being created:

class Animal:
    def __init__(self,type,colour,size):
        self.type =type
        self.colour = colour
        self.size = size

x = Animal("Dog","Black","12")    # x = variable to store the object,
# Object is instance of class to call the class.
print(x.type)
print(x.colour)
