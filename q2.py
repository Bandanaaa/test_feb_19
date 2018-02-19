"""
Create a class Circle which has a class variable PI with the value=22/7. Make two methods getArea and getCircumference inside this
 Circle class. Which when invoked returns area and circumference of each circle instances.
"""

class circle:
    pi=22/7
    def __index__(self,radius):
        self.radius=radius


    def getArea(self):
        return circle.pi*self.radius**2

    def getCircumference(self):
        return 2*circle.pi*self.radius

s=circle(5)
print(s.getArea())
print(s.getCircumference())