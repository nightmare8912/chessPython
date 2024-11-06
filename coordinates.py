# import copy
import math
# import sys
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # sys.setrecursionlimit(10000)

    def compare(self, c):
        return self.x == c.x and self.y == c.y

    def isValid(self):
        return (self.x >= 0 and self.y >= 0 and self.x <= 7 and self.y <= 7)
    
    def assignValue(self, x, y):
        self.x = x
        self.y = y

    def createNewCopy(self):
        # return copy.deepcopy(self)
        return Coordinates(self.x, self.y)

    def printCoordinates(self):
        print("(", self.y, ", ", self.x, "),", end = "")

    def getDistance(self, c1, c2):
        return math.sqrt(math.pow(c1.x - c2.x, 2) + math.pow(c1.y - c2.y, 2))
    
    