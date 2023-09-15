import coordinates
import pieces as pie
import accessories

class Board:
    def __init__(self):
        # self.piece = pie.Pieces("", "", coordinates.Coordinates(-1, -1))
        self.positions = [[pie.Pieces("", "", coordinates.Coordinates(-1, -1), 0) for _ in range(8)] for _ in range(8)]
        self.initializeBoard()

    def initializeBoard(self):
        self.placePawns(6, "white")
        self.placePiecesOtherThanPawns(7, "white")
        self.placePawns(1, "black")
        self.placePiecesOtherThanPawns(0, "black")

    def placePawns(self, row, color):
        for j in range(8):
            self.positions[row][j] = pie.Pieces("pawn", color, coordinates.Coordinates(row, j), 0)
    
    def placePiecesOtherThanPawns(self, row, color):
        for j in range(8):
            if (j == 0 or j == 7):
                self.positions[row][j] = pie.Pieces("rook", color, coordinates.Coordinates(row, j), 0)
            elif (j == 1 or j == 6):
                self.positions[row][j] = pie.Pieces("knight", color, coordinates.Coordinates(row, j), 0)
            elif (j == 2 or j == 5):
                self.positions[row][j] = pie.Pieces("bishop", color, coordinates.Coordinates(row, j), 0)
            elif (j == 3):
                self.positions[row][j] = pie.Pieces("king", color, coordinates.Coordinates(row, j), 0)
            elif (j == 4):
                self.positions[row][j] = pie.Pieces("queen", color, coordinates.Coordinates(row, j), 0)

    def drawBoard(self):
        accs = accessories.Accessories()
        print("\n")
        for i in range(8):
            accs.printInColor(str(i) + "\t", "b")
        print("\n")
        for i in range(8):
            for j in range(9):
                if (j != 8):
                    if (self.positions[i][j].pieceColor == "black"):
                        accs.printInColor(self.positions[i][j].pieceType + "\t", "r")
                    else:
                        print(self.positions[i][j].pieceType + "\t", end = "")
                else:
                    accs.printInColor(str(i), "b")
                accs.printInColor("", "w")
            print("\n")

    def drawBoardWithMoves(self, moves):
        accs = accessories.Accessories()
        print("\n")
        for i in range(8):
            accs.printInColor(str(i) + "\t", "b")
        print("\n")
        for point in moves:
                # print("lololol value is ", self.positions[point.x][point.y])
                if self.positions[point.x][point.y].pieceType == "":
                    self.positions[point.x][point.y].pieceType = "X"
        for i in range(8):
            for j in range(9):
                if (j != 8):
                    if (self.positions[i][j].pieceColor == "black"):
                        accs.printInColor(self.positions[i][j].pieceType + "\t", "r")
                    elif(self.positions[i][j].pieceType == "white"):
                        print(self.positions[i][j].pieceType + "\t", end = "")
                    elif(self.positions[i][j].pieceType == "X"):
                        accs.printInColor(self.positions[i][j].pieceType + "\t", "g")
                    else:
                        print(self.positions[i][j].pieceType + "\t", end = "")
                else:
                    accs.printInColor(str(i), "b")
                accs.printInColor("", "w")
            print("\n")
        for point in moves:
                if self.positions[point.x][point.y].pieceType == "X":
                    self.positions[point.x][point.y].pieceType = ""

    def getPieceAt(self, coord):
        return self.positions[coord.x][coord.y]