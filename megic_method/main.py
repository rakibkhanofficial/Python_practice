# Python program to show how to add two attributes

# Creating a class
class Method:
    def __init__(self, argument):
        self.attribute = argument

    # Creating a second class


class Method_2:
    def __init__(self, argument):
        self.attribute = argument
    # creating the instances


instance_1 = Method(" Attribute")
print(instance_1.attribute)
instance_2 = Method_2(" 27")
print(instance_2.attribute)

# Adding two attributes of the instances
print(instance_2.attribute + instance_1.attribute)  
