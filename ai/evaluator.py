import accessories
import coordinates

class Evaluator:
    def __init__(self, board):
        self.board = board
        self.accs = accessories.Accessories()

    # def getOppositeColor(self, color):
       
    #     if (color == "white"):
    #         return "black"    
    #     else:
    #         return "white"

    def getTrueScore(self, color):
        whiteScore = blackScore = 0
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == "white"):
                    whiteScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
                elif(self.board.getPieceAt(coord).pieceColor == "black"):
                    blackScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
        
        return whiteScore - blackScore

    def evaluateMove(self, src, dest, color):
        
        scoreBefore = self.getTrueScore(color)
        self.board.movePiece(src, dest)
        scoreAfter = self.getTrueScore(color)
        self.board.revertMove(src, dest)

        return scoreAfter - scoreBefore

