import coordinates
import pieces as pie
import accessories

class Board:
    def __init__(self):
        self.piece = pie.Pieces("", "", coordinates.Coordinates(-1, -1))
        self.postions = [[self.piece for _ in range(8)] for _ in range(8)]
        self.initializeBoard()

    def initializeBoard(self):
        self.placePawns(6, "white")
        self.placePiecesOtherThanPawns(7, "white")
        self.placePawns(1, "black")
        self.placePiecesOtherThanPawns(0, "black")

    def placePawns(self, row, color):
        for j in range(8):
            self.postions[row][j] = pie.Pieces("pawn", color, coordinates.Coordinates(row, j))
    
    def placePiecesOtherThanPawns(self, row, color):
        for j in range(8):
            if (j == 0 or j == 7):
                self.postions[row][j] = pie.Pieces("rook", color, coordinates.Coordinates(row, j))
            elif (j == 1 or j == 6):
                self.postions[row][j] = pie.Pieces("knight", color, coordinates.Coordinates(row, j))
            elif (j == 2 or j == 5):
                self.postions[row][j] = pie.Pieces("bishop", color, coordinates.Coordinates(row, j))
            elif (j == 3):
                self.postions[row][j] = pie.Pieces("king", color, coordinates.Coordinates(row, j))
            elif (j == 4):
                self.postions[row][j] = pie.Pieces("queen", color, coordinates.Coordinates(row, j))

    def drawBoard(self):
        accs = accessories.Accessories()
        print("\n")
        for i in range(8):
            accs.printInColor(str(i) + "\t", "b")
        print("\n")
        for i in range(8):
            for j in range(9):
                if (j != 8):
                    if (self.postions[i][j].pieceColor == "black"):
                        accs.printInColor(self.postions[i][j].pieceType + "\t", "r")
                    else:
                        print(self.postions[i][j].pieceType + "\t", end = "")
                else:
                    accs.printInColor(str(i), "b")
                accs.printInColor("", "w")
            print("\n")