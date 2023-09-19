import board as bd
import movements as mv
import coordinates
import accessories
from ai import engine as eng
from ai import evaluator as ev
import time
import sys
class Play:
    def __init__(self):
        sys.setrecursionlimit(100000)
        self.turn = "white"
        self.board = bd.Board()
        self.movements = mv.Movements(self.board)
        self.accs = accessories.Accessories()
        self.evaluator = ev.Evaluator(self.board)
        self.error = ""
    
    # !!!!!dont make turn in this function as global!!!!!
    def getOppositeTurn(self, turn):
        if (turn == "white"):
            return "black"
        else:
            return "white"

    def validateMove(self, src, dest):

        if (self.board.getPieceAt(src).pieceColor == ""):
            self.error = "Please choose piece "
            return False
        
        if (not self.movements.isMovementPossibleConsideringOnlyCheckAndIntersections(src, dest)):
            self.error = "Your move results in check "
            return False
        if (self.board.getPieceAt(src).pieceColor != self.turn):
            self.error = "Please move your piece "
            return False
        
        for i in self.movements.getAllPossibleMoves(src):
            if (i.compare(dest)):
                return True
        self.error = "Please chose a valid position to move"
        return False

    def isMate(self):
        allPossibleMoves = []
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                if (len(allPossibleMoves) > 0):
                    return False
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == self.turn):
                    if (len(self.movements.getPossibleMoves(coord)) != 0):
                        allPossibleMoves.append(self.movements.getPossibleMoves(coord))
        
        return True


    def humanPlaysHuman(self, src, dest):
        
        self.board.drawBoard(self.turn)
        if (self.isMate()):
            print()
            self.accs.printInColor("\nThe game is over and " + self.getOppositeTurn(self.turn) + " has won!!\n", "g")
            print()
        print("\n\nIts ", self.turn, "'s turn to move")
        self.accs.printInColor("Current score is: " + str(self.evaluator.evaluateBoard()) + "\n", "b")

        self.board.drawBoardWithMoves(self.turn, self.movements.getPossibleMoves(src))

        possibleMoves = self.movements.getPossibleMoves(src)
        print("Possible moves: ")
        for i in possibleMoves:
            i.printCoordinates()
        print()
        print("You want to move ", self.board.positions[src.x][src.y].pieceType, " of color ", self.board.getPieceAt(src).pieceColor)
        if (self.validateMove(src, dest)):
            self.printMovement(src, dest)
            self.board.movePiece(src, dest)
            print("piece was moved from ", end = "")
            src.printCoordinates()
            print("to ", end = "")
            dest.printCoordinates()
            self.turn = self.getOppositeTurn(self.turn)
            self.board.drawBoard(self.turn)
            # print("true was returned")
            return True
        else:
            self.accs.printInColor(self.error, 'r')
            return False
        
    def humanPlaysComputer(self, src, dest):

        self.board.drawBoard(self.turn)
        if (self.isMate()):
            print()
            self.accs.printInColor("\nThe game is over and " + self.getOppositeTurn(self.turn) + " has won!!\n", "g")
            print()
        print("\n\nIts ", self.turn, "'s turn to move")
        self.accs.printInColor("Current score is: " + str(self.evaluator.evaluateBoard()) + "\n", "b")

        self.board.drawBoardWithMoves(self.turn, self.movements.getPossibleMoves(src))

        possibleMoves = self.movements.getPossibleMoves(src)
        print("Possible moves: ")
        for i in possibleMoves:
            i.printCoordinates()
        print()
        print("You want to move ", self.board.positions[src.x][src.y].pieceType, " of color ", self.board.getPieceAt(src).pieceColor)
        if (self.validateMove(src, dest)):
            self.printMovement(src, dest)
            self.board.movePiece(src, dest)
            print("piece was moved from ", end = "")
            src.printCoordinates()
            print("to ", end = "")
            dest.printCoordinates()
            self.turn = self.getOppositeTurn(self.turn)
            self.board.drawBoard(self.turn)
            # print("true was returned")
            return True
        else:
            self.accs.printInColor(self.error, 'r')
            return False

    def printMovement(self, src, dest):
        print(self.board.getPieceAt(src).pieceColor + "'s "+ self.board.getPieceAt(src).pieceType +" was moved from ", end = "")
        src.printCoordinates()
        print(" to ", end = "")
        dest.printCoordinates()
        print()

    def returnPossibleMoves(self, coord):
        if (self.turn != self.board.getPieceAt(coord).pieceColor):
            return []
        else:
            return self.movements.getPossibleMoves(coord)
