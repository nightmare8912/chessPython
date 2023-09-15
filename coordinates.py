import copy
import math
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compare(self, c):
        return self.x == c.x and self.y == c.y

    def isValid(self):
        # self.printCoordinates(self)
        # if (self.x >= 0 and self.y >= 0 and self.x <= 7 and self.y <= 7):
        #     print(" is valid!!")
        # else:
        #     print(" is invalid")

        return (self.x >= 0 and self.y >= 0 and self.x <= 7 and self.y <= 7)
    
    def assignValue(self, x, y):
        self.x = x
        self.y = y

    def createNewCopy(self):
        return copy.deepcopy(self)

    def printCoordinates(self, c):
        print("( ", c.x, ", ", c.y, "), ", end = "")

    def getDistance(self, c1, c2):
        return math.sqrt(math.pow(c1.x - c2.x, 2) + math.pow(c1.y - c2.y, 2))