import board as bd
import movements as mv
import coordinates
import copy
class Play:
    def __init__(self):
        self.turn = "white"
        
    def getOppositeTurn(self, turn):
        if (turn == "white"):
            return "black"
        else:
            return "white"

    def movePiece(self, src, dest):

        self.board.positions[dest.x][dest.y] = copy.deepcopy(self.board.positions[src.x][src.y])
        self.board.positions[src.x][src.y].pieceType = ""
        self.board.positions[src.x][src.y].pieceColor = ""
        self.board.positions[src.x][src.y].timesMoved = 0

        self.board.positions[dest.x][dest.y].timesMoved += 1

        print("piece was moved ", self.board.positions[dest.x][dest.y].timesMoved, " times")

    def startPlaying(self):
        self.board = bd.Board()
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)
        movements = mv.Movements()

        while(True):
            self.board.drawBoard()
            print("\n\nIts ", self.turn, "'s turn to move\n\n")
            src.x = int(input("Enter x pos of piece to move: "))
            src.y = int(input("Enter y pos of piece to move: "))

            movements.updateBoard(copy.deepcopy(self.board))
            self.board.drawBoardWithMoves(movements.getPossibleMoves(self.board, src))

            print("Possible moves: ")
            for i in movements.getPossibleMoves(self.board, src):
                i.printCoordinates(i)
            print()
            print("You want to move ", self.board.positions[src.x][src.y].pieceType, " of color ", self.board.getPieceAt(src).pieceColor)
            dest.x = int(input("Enter x pos of where you want to to move: "))
            dest.y = int(input("Enter y pos of where you want to to move: "))


            movements.updateBoard(copy.deepcopy(self.board))
            if (movements.isMovementPossible(src, dest)):
                self.movePiece(src, dest)
            else:
                print("please choose a valid move")
                continue
            self.turn = self.getOppositeTurn(self.turn)
        
