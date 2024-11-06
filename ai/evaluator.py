import coordinates
import accessories
import pieces
class Evaluator:
    def __init__(self, board):
        self.board = board
        self.accs = accessories.Accessories()
    def evaluateBoard(self):

        whiteScore = blackScore = 0
        coord = coordinates.Coordinates(-1, -1)
        piece = pieces.Pieces("", "", coordinates.Coordinates(-1, -1), 0)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                piece.assignValue(self.board.getPieceAt(coord))
                if (piece.pieceColor == "black"):
                    blackScore += self.accs.getPieceWeightage(piece.pieceType)
                elif(piece.pieceColor == "white"):
                    whiteScore += self.accs.getPieceWeightage(piece.pieceType)

        return whiteScore - blackScore
