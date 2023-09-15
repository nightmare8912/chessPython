import coordinates

class Pieces:
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0

class King(Pieces):
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0
        
class Queen(Pieces):
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0

class Bishop(Pieces):
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0

class Knight(Pieces):
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0

class Rook(Pieces):
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0

class Pawn(Pieces):
    def __init__(self, pieceType, pieceColor, pieceCoordinates):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = 0