import board as bd
import movements as mv
import coordinates
import accessories as acs
from . import evaluator as ev
import random
import time
import copy

CHECKMATE = 99999

class Engine:
    def __init__(self, board, movements, engColor, intelligence):
        self.board = board
        self.movements = movements
        self.engColor = engColor
        self.depth = intelligence
        self.accs = acs.Accessories()
        self.evaluator = ev.Evaluator(self.board)
    
    def generateMove(self):
        self.accs.printInColor("Please wait while the Engine is thinking!\n", "g")
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        self.posEval = self.branchesPruned = 0
        start = time.time()
        # bestScore, bestMoves = self.minimax(self.engColor, self.depth)


        # bestScore, bestMoves = self.alphabeta1(self.engColor, -9999, 9999, self.depth)
        bestScore, bestMoves = self.alphabeta(self.engColor, -9999, 9999, self.depth)


        self.printMoves(bestMoves)
        self.accs.printInColor("Possible best moves: " + str(len(bestMoves)) + "\n", 'g')

        end = time.time()
        self.accs.printInColor("Positions Evaluated: " + str(self.posEval) + "\n", "y")
        self.accs.printInColor("Branches Pruned: " + str(self.branchesPruned) + "\n", "y")
        random.shuffle(bestMoves)
        
        self.accs.printInColor("Best score: " + str(bestScore) + "\n", 'g')
        self.accs.printInColor("Think time: " + str(end - start) + " seconds\n", 'p')
        src = bestMoves[0][0]
        dest = bestMoves[0][1]

        self.accs.playSound()

        return src, dest
    
    def minimax(self, color, depth):
        print(f"Minimax - Color: {color}, Depth: {depth}")
        if (depth == 0):
            return self.evaluator.evaluateBoard(), []
        # self.posEval += 1
        allMoves = self.getAllMoves(color)
        bestMove = []
        toBreak = False
        if (self.isMaximize(color)):
            maxEval = -9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    if (self.movements.isMate(self.getOppositeColor(color))):
                        maxEval = CHECKMATE
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(maxEval)]]
                        toBreak = True
                        self.board.revertMove(src, dest)
                        print("Checkmate was found!!!")
                        break
                    eval, temp = self.minimax(self.getOppositeColor(color), depth - 1)
                    self.posEval += 1
                    self.board.revertMove(src, dest)
                    if (eval > maxEval):
                        maxEval = eval
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(maxEval)]]
                    elif (eval == maxEval):
                        bestMove.append([src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(maxEval)])
                if (toBreak):
                    break
            print(f"MaxEval: {maxEval}, BestMove: ")
            self.printMoves(bestMove)
            return maxEval, bestMove
        
        else:
            minEval = 9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    if (self.movements.isMate(self.getOppositeColor(color))):
                        minEval = -CHECKMATE
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(minEval)]]
                        toBreak = True
                        self.board.revertMove(src, dest)
                        print("Checkmate was found!!!")
                        break
                    eval, temp = self.minimax(self.getOppositeColor(color), depth - 1)
                    self.posEval += 1
                    self.board.revertMove(src, dest)
                    if (eval < minEval):
                        minEval = eval
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(minEval)]]
                    elif (eval == minEval):
                        bestMove.append([src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(minEval)])
                if (toBreak):
                    break
            print(f"MinEval: {minEval}, BestMove: ")
            self.printMoves(bestMove)
            return minEval, bestMove

    def alphabeta(self, color, alpha, beta, depth):
        # print(f"ABPruning 1- Color: {color}, Alpha: {alpha}, Beta: {beta}, Depth: {depth}")
        if (depth == 0):
            return self.evaluator.evaluateBoard(), []
        # self.posEval += 1
        allMoves = self.getAllMoves(color)
        bestMove = []
        toBreak = False
        if (self.isMaximize(color)):
            maxEval = -9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    if (self.movements.isMate(self.getOppositeColor(color))):
                        maxEval = CHECKMATE
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(maxEval)]]
                        toBreak = True
                        self.board.revertMove(src, dest)
                        print("Checkmate was found!!!")
                        break
                    eval, temp = self.alphabeta(self.getOppositeColor(color), alpha, beta, depth - 1)
                    self.posEval += 1
                    self.board.revertMove(src, dest)
                    if (eval > maxEval):
                        maxEval = eval
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(maxEval)]]
                    elif (eval == maxEval):
                        bestMove.append([src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(maxEval)])
                    alpha = max(alpha, eval)
                    if (beta < alpha):
                        self.branchesPruned += 1
                        toBreak = True
                        break
                if (toBreak):
                    break
            # print(f"MaxEval: {maxEval}, Alpha: {alpha}, Beta: {beta}, BestMove:")
            # self.printMoves(bestMove)
            return maxEval, bestMove
        
        else:

            minEval = 9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    if (self.movements.isMate(self.getOppositeColor(color))):
                        minEval = -CHECKMATE
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(minEval)]]
                        toBreak = True
                        self.board.revertMove(src, dest)
                        print("Checkmate was found!!!")
                        break
                    eval, temp = self.alphabeta(self.getOppositeColor(color), alpha, beta, depth - 1)
                    self.posEval += 1
                    self.board.revertMove(src, dest)
                    if (eval < minEval):
                        minEval = eval
                        bestMove = [[src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(minEval)]]
                    if (eval == minEval):
                        bestMove.append([src.createNewCopy(), dest.createNewCopy(), copy.deepcopy(minEval)])
                    beta = min(beta, eval)
                    if (beta < alpha):
                        self.branchesPruned += 1
                        toBreak = True
                        break
                if (toBreak):
                    break
            # print(f"MinEval: {minEval}, Alpha: {alpha}, Beta: {beta}, BestMove:")
            # self.printMoves(bestMove)
            return minEval, bestMove

    def printMoves(self, moves):
        for move in moves:
            move[0].printCoordinates()
            print("--->", end = "")
            move[1].printCoordinates()
            print("-->Score:--> ", move[2])


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