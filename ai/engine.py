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
    def __init__(self, board, movements, engColor, intelligence, dynamicDepthEnabled):
        self.board = board
        self.movements = movements
        self.engColor = engColor
        self.depth = intelligence
        self.dynamicDepthCounter = 0
        self.accs = acs.Accessories()
        self.evaluator = ev.Evaluator(self.board)
        self.dynamicDepthEnabled = dynamicDepthEnabled
    
    def generateMove(self):
        self.accs.printInColor("This is a dynamic engine.\n", "p") if self.dynamicDepthEnabled else self.accs.printInColor("This is a non-dynamic engine.\n", "p")
        self.accs.printInColor("Please wait while the Engine is thinking!\n", "g")
        self.accs.printInColor("Engine depth at: " + str(self.depth) + "\n", "y")
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        self.posEval = self.branchesPruned = 0
        self.start = time.time()
        bestScore, bestMoves = self.alphabeta(self.engColor, -9999, 9999, self.depth)

        self.end = time.time()
        self.accs.printInColor("\nPositions Evaluated: " + str(self.posEval) + "\n", "y")
        self.accs.printInColor("Branches Pruned: " + str(self.branchesPruned) + "\n", "g")
        
        random.shuffle(bestMoves)
        
        self.accs.printInColor("Best score: " + str(bestScore) + "\n", 'g')
        self.accs.printInColor("Think time: " + str(round(self.end - self.start, 2)) + " seconds or " + str(round((self.end - self.start) / 60, 2)) + " minutes\n", 'p')
        if (self.dynamicDepthEnabled):
            if (round(self.end - self.start, 2) < 3.0):
                self.dynamicDepthCounter += 1
                if self.dynamicDepthCounter > 3:
                    self.depth += 1
                    self.accs.printInColor("Increasing depth of engine to " + str(self.depth) + ".\n", "g")
                    self.dynamicDepthCounter = 0
            elif (round(self.end - self.start, 2) > 15.0):
                self.dynamicDepthCounter -= 1
                if self.dynamicDepthCounter < 0 and self.depth > 1:
                    self.depth -= 1
                    self.accs.printInColor("Decreasing depth of engine to " + str(self.depth) + ".\n", "r")
                    self.dynamicDepthCounter = 0
        try:
            src.x = bestMoves[0][0][0]
            src.y = bestMoves[0][0][1]
            dest.x = bestMoves[0][1][0]
            dest.y = bestMoves[0][1][1]
        except:
            my_dict = self.getAllMoves(self.engColor)
            src = random.choice(list(my_dict))
            dest = my_dict[src][0]
            time.sleep(5)
            self.accs.printInColor("\n\n\n!!!EXCEPTION RAISED NO BEST MOVES FOUND AND RANDOM MOVE WAS MADE!!!\n\n\n", 'r')

        self.accs.playSound()

        return src, dest
 
    def alphabeta(self, color, alpha, beta, depth):
        if (depth == 0):
            return self.evaluator.evaluateBoard(), [[]]
        allMoves = self.getAllMoves(color)
        bestMove = []
        toBreak = False
        if (self.isMaximize(color)):
            maxEval = -9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    self.posEval += 1
                    try:
                        # putting this is try except because the time (time.time() - self.start) can be 0 sometimes, as the moves are made very fast so this can raise error
                        toPrint = "Positions evaluated: " + str(self.posEval) + "   Searching at depth: " + str(depth) + "   Positions per second: " + str(self.posEval / (time.time() - self.start))
                        self.accs.print_and_update(toPrint, len(toPrint), 'p')
                    except ZeroDivisionError:
                        pass
                    eval, _ = self.alphabeta(self.getOppositeColor(color), alpha, beta, depth - 1)
                    self.board.revertMove(src, dest)
                    if (eval > maxEval):
                        maxEval = eval
                        bestMove = [((src.x, src.y), (dest.x, dest.y), maxEval)]
                    elif (eval == maxEval):
                        bestMove.append(((src.x, src.y), (dest.x, dest.y), maxEval))
                    alpha = max(alpha, eval)
                    if (beta < alpha):
                        self.branchesPruned += 1
                        toBreak = True
                        break
                if (toBreak):
                    break
            return maxEval, bestMove
        
        else:
            minEval = 9999
            for src in allMoves:
                for dest in allMoves[src]:
                    self.board.movePiece(src, dest)
                    self.posEval += 1
                    try:
                        # putting this is try except because the time (time.time() - self.start) can be 0 sometimes, as the moves are made very fast so this can raise error
                        toPrint = "Positions evaluated: " + str(self.posEval) + "   Searching at depth: " + str(depth) + "   Positions per second: " + str(self.posEval / (time.time() - self.start))
                        self.accs.print_and_update(toPrint, len(toPrint), 'p')
                    except ZeroDivisionError:
                        pass
                    eval, _ = self.alphabeta(self.getOppositeColor(color), alpha, beta, depth - 1)
                    self.board.revertMove(src, dest)
                    if (eval < minEval):
                        minEval = eval
                        bestMove = [((src.x, src.y), (dest.x, dest.y), minEval)]
                    if (eval == minEval):
                        bestMove.append(((src.x, src.y), (dest.x, dest.y), minEval))
                    beta = min(beta, eval)
                    if (beta < alpha):
                        self.branchesPruned += 1
                        toBreak = True
                        break
                if (toBreak):
                    break
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
                    possibleMoves = self.movements.getPossibleMoves(coord)
                    if (len(possibleMoves) > 0):
                        allMoves[coord.createNewCopy()] = possibleMoves
        return allMoves
    
    def getOppositeColor(self, color):
        return "black" if color == "white" else "white"