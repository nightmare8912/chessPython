import board as bd
import movements as mv
import coordinates
import accessories as acs
from . import evaluator as ev

class Engine:
    def __init__(self, board, movements, engColor):
        self.board = board
        self.movements = movements
        self.engColor = engColor
        self.accs = acs.Accessories()
        self.evaluator = ev.Evaluator(self.board)
    
    def generateMove(self):
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        bestScore, bestMove = self.minimax(self.engColor, 3)

        self.accs.printInColor("\nBest score: " + str(bestScore) + "\n", 'g')
        src = bestMove[0]
        dest = bestMove[1]

        return src, dest
    
    def minimax(self, color, depth):
        if (depth == 0):
            return self.evaluator.evaluateBoard(), []

        allMoves = self.getAllMoves(color)
        bestMove = []
        if (self.isMaximize(color)):
            maxEval = -9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    eval, temp = self.minimax(self.getOppositeColor(color), depth - 1)
                    self.board.revertMove(src, dest)
                    if (eval > maxEval):
                        maxEval = eval
                        bestMove = [src.createNewCopy(), dest.createNewCopy()]
            return maxEval, bestMove
        
        else:
            minEval = 9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    eval, temp = self.minimax(self.getOppositeColor(color), depth - 1)
                    self.board.revertMove(src, dest)
                    if (eval < minEval):
                        minEval = eval
                        bestMove = [src.createNewCopy(), dest.createNewCopy()]
            return minEval, bestMove

    def isMaximize(self, color):
        return color == "white"
    
    def getAllMoves(self, color):
        allMoves = {}
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == color):
                    if (len(self.movements.getPossibleMoves(coord)) > 0):
                        allMoves[coord.createNewCopy()] = self.movements.getPossibleMoves(coord)
        return allMoves
    
    def getOppositeColor(self, color):
        if (color == "white"):
            return "black"
        return "white"