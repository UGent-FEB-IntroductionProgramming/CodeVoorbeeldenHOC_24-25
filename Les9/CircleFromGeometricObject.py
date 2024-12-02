from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius, color = "green", filled = True, bold = True ):
        super().__init__(color,filled, bold)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 2 * self.__radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(super().__str__() + " radius: " + str(self.__radius))

    def __str__(self):
        return super().__str__() + " radius: " + str(self.__radius)

#a = Circle(7);
#print(a)