from turtle import *

# Use a class to define the shape, and then take size and name 

class Shape():
    """Class for init of the shape"""

    t = Turtle()
    
    def __init__(self, size, name, colour):
        self.shape = shape
        self.name = name
        self.colour = colour

    def __str__(self):
        return f'Size: {self.size}, Name: {self.name}, Colour: {self.colour}'

    def square(self):
        size = self.size
        colour = self.colour
        forward(50)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(50)


# Make Circle definition
# Create definition for generic shape, with sides n
# done!