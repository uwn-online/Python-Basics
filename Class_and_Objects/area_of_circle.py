"""Create a circle class that will take value of a radius and return the area of the circle"""
import math 
class Circle(object):
    """Represents a circle with radius. Calculate area"""
    def __init__(self, radius):
        self.radius = radius
    def calc_area(self): # The methods uses math module to calc the area.
        area = math.pi * (self.radius)**2
        return area
circle1 = Circle(8)
print(circle1.calc_area()) # Call the method to return the area of the circle.



