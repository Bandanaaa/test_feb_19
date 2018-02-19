"""
Create a RectangleGeometry class which takes in length and breadth as initialize parameter.
Make two methods getArea and getPerimeter inside this class.
Which when invoked returns area and perimeter of each rectangle instance.
"""
class RectangleGeometry(object):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

    def getPerimeter(self):
        return 2*(self.length + self.breadth)


rect = RectangleGeometry(5, 4)
print(rect.getArea())
print(rect.getPerimeter())