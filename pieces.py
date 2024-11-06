class Pieces:
    def __init__(self, pieceType, pieceColor, pieceCoordinates, timesMoved):
        self.pieceType = pieceType
        self.pieceColor = pieceColor
        self.pieceCoordinates = pieceCoordinates
        self.timesMoved = timesMoved
    
    def assignValue(self, piece):
        self.pieceType = piece.pieceType
        self.pieceColor = piece.pieceColor
        self.pieceCoordinates = piece.pieceCoordinates
        self.timesMoved = piece.timesMoved

    def createNewCopy(self):
        return Pieces(self.pieceType, self.pieceColor, self.pieceCoordinates, self.timesMoved)