import board as bd
import movements as mv
import coordinates
import accessories
import sys
class Play:
    def __init__(self):
        sys.setrecursionlimit(10000)
        self.turn = "white"
        self.board = bd.Board()
        self.movements = mv.Movements(self.board)
        self.accs = accessories.Accessories()
        self.error = ""
        
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
            i.printCoordinates()
            src.printCoordinates()
            print()
            if (i.compare(dest)):
                return True
        self.error = "Please chose a valid position to move"
        return False

    def startPlaying(self):
        
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        while(True):
            self.board.drawBoard()
            print("\n\nIts ", self.turn, "'s turn to move\n\n")
            src.x = int(input("Enter x pos of piece to move: "))
            src.y = int(input("Enter y pos of piece to move: "))

            self.board.drawBoardWithMoves(self.movements.getPossibleMoves(src))

            possibleMoves = self.movements.getPossibleMoves(src)
            print("Possible moves: ")
            for i in possibleMoves:
                i.printCoordinates()
            print()
            print("You want to move ", self.board.positions[src.x][src.y].pieceType, " of color ", self.board.getPieceAt(src).pieceColor)
            dest.x = int(input("Enter x pos of where you want to to move: "))
            dest.y = int(input("Enter y pos of where you want to to move: "))

            if (self.validateMove(src, dest)):
                self.board.movePiece(src, dest)
            else:
                self.accs.printInColor(self.error, 'r')
                continue
            self.turn = self.getOppositeTurn(self.turn)
        