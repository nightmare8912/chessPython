import board as bd
import movements as mv
import coordinates
import evaluator as ev

class smartEngine:
    def __init__(self, board, movements):
        self.board = board
        self.movements = movements
        self.depth = 4
        self.engColor = "black"
        self.evaluator = ev.Evaluator(self.board)
    
    def getOppositeColor(self, color):
        if (color == "white"):
            return "black"
        return "white"

    def moveAndEvaluate(self, src, dest):
        
        beforeScore = self.evaluator.evaluateBoard()
        self.board.movePiece(src, dest)
        afterScore = self.evaluator.evaluateBoard()
        # self.board.revertMove(src, dest)

        return beforeScore - afterScore
        

    # def recursivelyMakeMoves(self, depth, color, allMovesAfterDepthIsReached):
    #     if (depth <= 0):
    #         bestMove = [-9999]
    #         currIndex = 0
    #         for move in allMovesAfterDepthIsReached:
    #             if (move[0] > bestMove[0]):
    #                 bestMove = move
    #             currIndex += 1
    #         return bestMove

        

    #     return self.recursivelyMakeMoves(depth - 1, self.getOppositeColor(color), allMovesAfterDepthIsReached)
        
    def recursivelyMakeMoves(self, depth, color):
        bestMoveForWhite = bestMoveForBlack = [-9999]
        if (depth <= 0):
            allPossibleMoves = self.getAllMoves(color)
            currIndex = 0
            for move in allPossibleMoves:
                if (color == "white" and move[0] > bestMoveForWhite[0]):
                    bestMoveForWhite = move
                elif (color == "black" and move[0] < bestMoveForBlack[0]):
                    bestMoveForBlack = move
                currIndex += 1
            return bestMoveForWhite, bestMoveForBlack

        allPossibleMoves = self.getAllMoves(color)
        for move in allPossibleMoves:
            # movesForWhite, movesForBlack = self.recursivelyMakeMoves(depth - 1, self.getOppositeColor(color))
            self.board.movePiece(move[1], move[2])
            self.recursivelyMakeMoves(depth - 1,self.getOppositeColor(color))
        return bestMoveForWhite, bestMoveForBlack
        
    def getBestMove(self):
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)
        turn = self.engColor

        return src, dest
    
    def getAllMoves(self, color):
        allMoves = []
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == color):
                    allMoves.append([coord.createNewCopy(), self.movements.getPossibleMoves(coord)])
        return allMoves
    
    