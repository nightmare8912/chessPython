import board as bd
import movements as mv
import coordinates
import accessories as acs
from . import evaluator as ev
import random
import time
import sys

class engine:
    def __init__(self, board, movements, engColor, depth = 2):
        self.board = board
        self.movements = movements
        self.engColor = engColor
        self.depth = depth
        self.accs = acs.Accessories()
        self.evaluator = ev.Evaluator(self.board)
        sys.setrecursionlimit(100000)

    def generateMove(self):
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        start = time.time()
        self.counter = 0
        bestScore = self.minimax(0, self.engColor)
        end = time.time()
        print("fn was called ", self.counter, " times")
        bestMoves = self.findAllMovesWithGivenScore(bestScore)

        print("best score: ", bestScore)
        print("best moves: ", bestMoves)
        if (len(bestMoves) == 0):
            moves = self.getAllMoves(self.engColor)
            for src in moves:
                for dest in moves[src]:
                    bestMoves.append([src.createNewCopy(), dest.createNewCopy()])
            self.accs.printInColor("\nNo best moves were found!!!\n", "r")
        for move in bestMoves:
            for coord in move:
                coord.printCoordinates()
            print()

        randomIndex = random.randint(0, len(bestMoves) - 1)

        src = bestMoves[randomIndex][0]
        dest = bestMoves[randomIndex][1]
        self.accs.printInColor("\nTime elapsed: " + str(end - start) + "seconds\n", 'g')
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
        return color == "white"

    def minimax(self, depth, color):
        self.counter += 1
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
