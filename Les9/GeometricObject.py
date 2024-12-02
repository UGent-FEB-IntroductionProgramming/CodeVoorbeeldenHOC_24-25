class GeometricObject:
    def __init__(self, color = "green", filled = True, bold = True):
        self.__color = color
        self.__filled = filled
        self.__bold = bold

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled) + \
            " and bold: " + str(self.__bold)
