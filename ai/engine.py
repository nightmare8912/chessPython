import board as bd
import movements as mv
import coordinates
import accessories as acs
from . import evaluator as ev
import random

class engine:
    def __init__(self, board, movements, engColor, depth = 2):
        self.board = board
        self.movements = movements
        self.engColor = engColor
        self.depth = depth
        self.accs = acs.Accessories()
        self.evaluator = ev.Evaluator(self.board)

    def generateMove(self):
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        bestScore = self.minimax(0, self.engColor)
        bestMoves = self.findAllMovesWithGivenScore(bestScore)

        print("best score: ", bestScore)
        print("best moves: ", bestMoves)
        if (len(bestMoves) == 0):
            bestMoves = self.getAllMoves(self.engColor)
            self.accs.printInColor("\nNo best moves were found!!!\n", "r")
        for move in bestMoves:
            for coord in move:
                coord.printCoordinates()
            print()

        randomIndex = random.randint(0, len(bestMoves) - 1)

        src = bestMoves[randomIndex][0]
        dest = bestMoves[randomIndex][1]

        return src, dest
    
    def findAllMovesWithGivenScore(self, givenScore):
        moves = []
        allMoves = self.getAllMoves(self.engColor)
        for src in allMoves:
            for dest in allMoves[src]:
                score = self.makeMoveAndEvaluate(src, dest)
                self.board.revertMove(src, dest)
                if (score == givenScore):
                    moves.append([src.createNewCopy(), dest.createNewCopy()])

        return moves
    def makeMoveAndEvaluate(self, src, dest):
        beforeScore = self.evaluator.evaluateBoard()
        self.board.movePiece(src, dest)
        afterScore = self.evaluator.evaluateBoard()
        return afterScore - beforeScore

    def toMaximize(self, color):
        # if (self.engColor == color == "white"):
        #     return 1
        # elif (self.engColor == color == "black"):
        #     return 2
        # elif (self.engColor != color and color == "white"):
        #     return 3
        # elif (self.engColor != color and color == "black"):
        #     return 4
        return color == "white"

    def minimax(self, depth, color):
        allMoves = self.getAllMoves(color)
        maxScore = -9999
        minScore = 9999  
        if (depth >= self.depth):
            for src in allMoves:
                for dest in allMoves[src]:
                    score = self.makeMoveAndEvaluate(src, dest)
                    self.board.revertMove(src, dest)
                    if (self.toMaximize(color)):
                        maxScore = max(score, maxScore)
                    else:
                        minScore = min(score, minScore)
            if (self.toMaximize(color)):
                return maxScore
            else:
                return minScore
        for src in allMoves:
            for dest in allMoves[src]:
                self.board.movePiece(src, dest)
                score = self.minimax(depth + 1, self.getOppositeColor(color))
                self.board.revertMove(src, dest)
                if (self.toMaximize(color)):
                    maxScore = max(score, maxScore)
                else:
                    minScore = min(score, minScore)
        if (self.toMaximize(color)):
            return maxScore
        else:
            return minScore

    # delete it in future
    def printAllMoves(self, allMoves):
        for src in allMoves:
            src.printCoordinates()
            print("------>", end = "")
            for moves in allMoves[src]:
                moves.printCoordinates()
            print()

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
    
    # def minimax(self, depth, color):
        # if (depth >= self.depth):
        #         return
        #     allMoves = self.getAllMoves(color)
        #     max = -9999
        #     min = 9999
        #     bestMove = [] # this will contain [[src1, dest1], [src2, dest2] ..., [srcN, destN]] if multiple best moves possible
        #     for src in allMoves:
        #         for dest in src:
        #             scoreChange = self.makeMoveAndEvaluate(src, dest)
        #             if (self.toMaximize(color) == 1 or self.toMaximize(color) == 4):
        #                 if (scoreChange > max):
        #                     max = scoreChange
        #                     bestMove = [[src, dest]]
        #                 elif (scoreChange == max):
        #                     bestMove.append([src, dest])
        #                 self.minimax(depth + 1, self.getOppositeColor(color))

        #             elif (self.toMaximize(color) == 2 or self.toMaximize(color) == 3):
        #                 if (scoreChange < min):
        #                     min = scoreChange
        #                     bestMove = [[src, dest]]
        #                 elif (scoreChange == min):
        #                     bestMove.append([src, dest])
        #                 self.minimax(depth + 1, self.getOppositeColor(color))