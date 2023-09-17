import coordinates
import accessories

class Evaluator:
    def __init__(self, board):
        self.board = board
        self.accs = accessories.Accessories()

    def evaluateBoard(self):

        whiteScore = blackScore = 0
        coord = coordinates.Coordinates(-1, -1)

        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(i, j).pieceColor == "black"):
                    blackScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
                elif(self.board.getPieceAt(i, j).pieceColor == "white"):
                    whiteScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)

        return whiteScore - blackScore
