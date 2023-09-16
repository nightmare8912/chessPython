import board as bd
import movements as mv
import coordinates
import accessories as acs

class Engine:
    def __init__(self, board, movements):
        self.board = board
        self.movements = movements
        self.accs = acs.Accessories()

    def analyzeBoard(self):
        whiteScore = 0
        blackScore = 0
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceType != ""):
                    if (self.board.getPieceAt(coord).pieceColor == "white"):
                        whiteScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
                    else:
                        blackScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
        return whiteScore, blackScore

    def getEveryPossibleMove(self):
        allPossibleMoves = {}
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == "black"):
                    # print(f"moves calculated for {self.board.getPieceAt(coord).pieceColor}'s {self.board.getPieceAt(coord).pieceType}")
                    allPossibleMoves[coord.createNewCopy()] = self.movements.getPossibleMoves(coord)     
        return allPossibleMoves

    def generateMove(self):

        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        bestScore = -9999
        bestMove = []
        whiteScore = 0
        blackScore = 0

        allPossibleMoves = self.getEveryPossibleMove()
        for move in allPossibleMoves:
            src = move
            # print(f"moves calculated for {self.board.getPieceAt(src).pieceColor}'s {self.board.getPieceAt(src).pieceType}")
            for j in allPossibleMoves[move]:
                dest = j
                self.board.movePiece(src, dest)
                whiteScore, blackScore = self.analyzeBoard()
                if (blackScore - whiteScore > bestScore):
                    bestScore = blackScore - whiteScore
                    if (len(bestMove) != 0):
                        bestMove.pop()
                    bestMove.append([src, dest])
                self.board.revertMove(src, dest)

        src = bestMove[0][0]
        dest = bestMove[0][1]

        return src, dest