
import board as bd
import movements as mv
import coordinates
import accessories as acs
import random as rd

class Engine:
    def __init__(self, board, movements, computerColor):
        self.board = board
        self.movements = movements
        self.computerColor = computerColor
        self.accs = acs.Accessories()

    def getOppositeColor(self, color):
       
        if (color == "white"):
            return "black"
        else:
            return "white"

    def analyzeBoard(self):
        whiteScore = 0
        blackScore = 0
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceType != ""):
                    if (self.board.getPieceAt(coord).pieceColor == self.getOppositeColor(self.computerColor)):
                        whiteScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
                    else:
                        blackScore += self.accs.getPieceWeightage(self.board.getPieceAt(coord).pieceType)
        return whiteScore, blackScore

    def getEveryPossibleMove(self, color):
        allPossibleMoves = {}
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == color):
                    # print(f"moves calculated for {self.board.getPieceAt(coord).pieceColor}'s {self.board.getPieceAt(coord).pieceType}")
                    allPossibleMoves[coord.createNewCopy()] = self.movements.getPossibleMoves(coord)     
        return allPossibleMoves

    def calculateScore(self, whiteScore, blackScore):
        if (self.computerColor == "white"):
            return whiteScore - blackScore
        else:
            return blackScore - whiteScore

    def generateMove(self, color):

        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        bestScore = -9999
        bestMove = []
        whiteScore = 0
        blackScore = 0

        allPossibleMoves = self.getEveryPossibleMove(self.computerColor)
        for move in allPossibleMoves:
            src = move
            # print(f"moves calculated for {self.board.getPieceAt(src).pieceColor}'s {self.board.getPieceAt(src).pieceType}")
            for j in allPossibleMoves[move]:
                dest = j
                self.board.movePiece(src, dest)
                whiteScore, blackScore = self.analyzeBoard()
                if (self.calculateScore(whiteScore, blackScore) >= bestScore):
                    bestScore = self.calculateScore(whiteScore, blackScore)
                    bestMove.append([src, dest, bestScore])
                    j = 0
                    for i in bestMove:
                        if (i[j][2] < bestScore):
                            i.pop(j)
                    j += 1

                self.board.revertMove(src, dest)
        random = rd.randint(0, len(bestMove) - 1)
        src = bestMove[random][0]
        dest = bestMove[random][1]

        return src, dest