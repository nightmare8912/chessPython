class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compare(self, c):
        return self.x == c.x and self.y == c.y