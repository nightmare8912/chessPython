import coordinates
import pieces as pie
import accessories
import copy
import sys

class Board:
    def __init__(self):
        sys.setrecursionlimit(10000)
        self.positions = [[pie.Pieces("", "", coordinates.Coordinates(-1, -1), 0) for _ in range(8)] for _ in range(8)]
        self.initializeBoard()
        self.movesLog = []
        self.accs = accessories.Accessories()

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
                self.positions[row][j] = pie.Pieces("queen", color, coordinates.Coordinates(row, j), 0)
            elif (j == 4):
                self.positions[row][j] = pie.Pieces("king", color, coordinates.Coordinates(row, j), 0)

    def drawBoard(self, color):
        if (color == "white"):
            self.drawBoardForWhite()
        else:
            self.drawBoardForBlack()
    
    def drawBoardWithMoves(self, color, moves):
        if (color == "white"):
            self.drawBoardWithMovesForWhite(moves)
        else:
            self.drawBoardWithMovesForBlack(moves)
    
    # this is probably the most messy code i have written in my life, and i ve no idea how on earth is this working
    def drawBoardWithMovesForWhite(self, moves):
        print("\n")
        self.accs.printSpaces(20)
        for i in range(8):
            if (i != 4):
                self.accs.printInColor('\t--', 'p')
            else:
                self.accs.printInColor('\tx', 'y')
        print("\n")
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        for point in moves:
                if self.positions[point.x][point.y].pieceType == "":
                    self.positions[point.x][point.y].pieceType = "X"
        for i in range(8):
            self.accs.printSpaces(10)
            if (i != 4):
                self.accs.printInColor('|', 'p')
            else:
                self.accs.printInColor('y', 'y')
            self.accs.printSpaces(9)
            for j in range(9):
                if (j == 0):
                    self.accs.printInColor("|", 'b')
                if (j != 8):
                    if (self.positions[i][j].pieceColor == "black"):
                        self.accs.printInColor(self.positions[i][j].pieceType, "r")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        # self.accs.printInColor(str(len(self.positions[i][j].pieceType)), 'g')
                        self.accs.printInColor("|", 'b')
                    elif (self.positions[i][j].pieceColor == "white"):
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        self.accs.printInColor("|", 'b')
                    elif (self.positions[i][j].pieceType == "X"):
                        self.accs.printSpaces(3)
                        self.accs.printInColor(self.positions[i][j].pieceType, 'g')
                        self.accs.printSpaces(2)
                        self.accs.printInColor("|", 'b')
                    else:
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6)
                        self.accs.printInColor("|", 'b')
                else:
                    self.accs.printSpaces(3)
                    self.accs.printInColor(str(i), "y")
                    self.accs.printSpaces(2)
                    self.accs.printInColor("|", 'b')
                self.accs.printInColor("", "w")
            print()
            self.accs.printSpaces(20)
            for _ in range(9):
                self.accs.printInColor("+", 'b')
                for _ in range(6):
                    self.accs.printInColor("-", 'b')
            self.accs.printInColor("+", 'b')
            if i != 7:
                print()
        print()
        self.accs.printSpaces(20)
        for i in range(10):
            if (i != 9):
                self.accs.printInColor("|", 'b')
                self.accs.printSpaces(3)
                self.accs.printInColor(str(i), 'y')
                self.accs.printSpaces(2)
            else:
                self.accs.printInColor("|", 'b')
        print()
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        print("\n")
        for point in moves:
                if self.positions[point.x][point.y].pieceType == "X":
                    self.positions[point.x][point.y].pieceType = ""

    def drawBoardForWhite(self):
        print("\n")
        print()
        self.accs.printSpaces(20)
        for i in range(8):
            if (i != 4):
                self.accs.printInColor('\t--', 'p')
            else:
                self.accs.printInColor('\tx', 'y')
        print("\n")
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        for i in range(8):
            self.accs.printSpaces(10)
            if (i != 4):
                self.accs.printInColor('|', 'p')
            else:
                self.accs.printInColor('y', 'y')
            self.accs.printSpaces(9)
            for j in range(9):
                if (j == 0):
                    self.accs.printInColor("|", 'b')
                if (j != 8):
                    if (self.positions[i][j].pieceColor == "black"):
                        self.accs.printInColor(self.positions[i][j].pieceType, "r")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        # self.accs.printInColor(str(len(self.positions[i][j].pieceType)), 'g')
                        self.accs.printInColor("|", 'b')
                    elif (self.positions[i][j].pieceColor == "white"):
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        self.accs.printInColor("|", 'b')
                    else:
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6)
                        self.accs.printInColor("|", 'b')
                else:
                    self.accs.printSpaces(3)
                    self.accs.printInColor(str(i), "y")
                    self.accs.printSpaces(2)
                    self.accs.printInColor("|", 'b')
                self.accs.printInColor("", "w")
            print()
            self.accs.printSpaces(20)
            for _ in range(9):
                self.accs.printInColor("+", 'b')
                for _ in range(6):
                    self.accs.printInColor("-", 'b')
            self.accs.printInColor("+", 'b')
            if i != 7:
                print()
        print()
        self.accs.printSpaces(20)
        for i in range(10):
            if (i != 9):
                self.accs.printInColor("|", 'b')
                self.accs.printSpaces(3)
                self.accs.printInColor(str(i), 'y')
                self.accs.printSpaces(2)
            else:
                self.accs.printInColor("|", 'b')
        print()
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        print("\n")

    def drawBoardWithMovesForBlack(self, moves):
        print("\n")
        self.accs.printSpaces(20)
        for i in range(8):
            if (i != 4):
                self.accs.printInColor('\t--', 'p')
            else:
                self.accs.printInColor('\tx', 'y')
        print("\n")
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        for point in moves:
                if self.positions[point.x][point.y].pieceType == "":
                    self.positions[point.x][point.y].pieceType = "X"
        for i in range(7, -1, -1):
            self.accs.printSpaces(10)
            if (i != 4):
                self.accs.printInColor('|', 'p')
            else:
                self.accs.printInColor('y', 'y')
            self.accs.printSpaces(9)
            for j in range(9):
                if (j == 0):
                    self.accs.printInColor("|", 'b')
                if (j != 8):
                    if (self.positions[i][j].pieceColor == "black"):
                        self.accs.printInColor(self.positions[i][j].pieceType, "r")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        # self.accs.printInColor(str(len(self.positions[i][j].pieceType)), 'g')
                        self.accs.printInColor("|", 'b')
                    elif (self.positions[i][j].pieceColor == "white"):
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        self.accs.printInColor("|", 'b')
                    elif (self.positions[i][j].pieceType == "X"):
                        self.accs.printSpaces(3)
                        self.accs.printInColor(self.positions[i][j].pieceType, 'g')
                        self.accs.printSpaces(2)
                        self.accs.printInColor("|", 'b')
                    else:
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6)
                        self.accs.printInColor("|", 'b')
                else:
                    self.accs.printSpaces(3)
                    self.accs.printInColor(str(i), "y")
                    self.accs.printSpaces(2)
                    self.accs.printInColor("|", 'b')
                self.accs.printInColor("", "w")
            print()
            self.accs.printSpaces(20)
            for _ in range(9):
                self.accs.printInColor("+", 'b')
                for _ in range(6):
                    self.accs.printInColor("-", 'b')
            self.accs.printInColor("+", 'b')
            # if i != 0:
            print()
        # print()
        self.accs.printSpaces(20)
        for i in range(10):
            if (i != 9):
                self.accs.printInColor("|", 'b')
                self.accs.printSpaces(3)
                if (i != 8):
                    self.accs.printInColor(str(i), 'y')
                    self.accs.printSpaces(2)
                else:
                    self.accs.printSpaces(3)
            else:
                self.accs.printInColor("|", 'b')
        print()
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        print("\n")
        for point in moves:
                if self.positions[point.x][point.y].pieceType == "X":
                    self.positions[point.x][point.y].pieceType = ""

    def drawBoardForBlack(self):
        print("\n")
        self.accs.printSpaces(20)
        for i in range(8):
            if (i != 4):
                self.accs.printInColor('\t--', 'p')
            else:
                self.accs.printInColor('\tx', 'y')
        print("\n")
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        for i in range(7, -1, -1):
            self.accs.printSpaces(10)
            if (i != 4):
                self.accs.printInColor('|', 'p')
            else:
                self.accs.printInColor('y', 'y')
            self.accs.printSpaces(9)
            for j in range(9):
                if (j == 0):
                    self.accs.printInColor("|", 'b')
                if (j != 8):
                    if (self.positions[i][j].pieceColor == "black"):
                        self.accs.printInColor(self.positions[i][j].pieceType, "r")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        # self.accs.printInColor(str(len(self.positions[i][j].pieceType)), 'g')
                        self.accs.printInColor("|", 'b')
                    elif (self.positions[i][j].pieceColor == "white"):
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6 - len(self.positions[i][j].pieceType))
                        self.accs.printInColor("|", 'b')
                    else:
                        print(self.positions[i][j].pieceType, end = "")
                        self.accs.printSpaces(6)
                        self.accs.printInColor("|", 'b')
                else:
                    self.accs.printSpaces(3)
                    self.accs.printInColor(str(i), "y")
                    self.accs.printSpaces(2)
                    self.accs.printInColor("|", 'b')
                self.accs.printInColor("", "w")
            print()
            self.accs.printSpaces(20)
            for _ in range(9):
                self.accs.printInColor("+", 'b')
                for _ in range(6):
                    self.accs.printInColor("-", 'b')
            self.accs.printInColor("+", 'b')
            # if i != 0:
            print()
        # print()
        self.accs.printSpaces(20)
        for i in range(10):
            if (i != 9):
                self.accs.printInColor("|", 'b')
                self.accs.printSpaces(3)
                if (i != 9):
                    self.accs.printInColor(str(i), 'y')
                    self.accs.printSpaces(2)
                else:
                    self.accs.printSpaces(3)
            else:
                self.accs.printInColor("|", 'b')
        print()
        self.accs.printSpaces(20)
        for _ in range(9):
            self.accs.printInColor("+", 'b')
            for _ in range(6):
                self.accs.printInColor("-", 'b')
        self.accs.printInColor("+", 'b')
        print()
        print("\n")

    def getPieceAt(self, coord):
        if (coord.isValid()):
            return self.positions[coord.x][coord.y]
        else:
            return pie.Pieces("", "", "", "")
    
    def logMoves(self, src, dest):
        # self.movesLog.append([copy.deepcopy(self.positions[src.x][src.y]), copy.deepcopy(self.positions[dest.x][dest.y])])
        self.movesLog.append([self.positions[src.x][src.y].createNewCopy(), self.positions[dest.x][dest.y].createNewCopy()])

    def movePiece(self, src, dest):

        self.positions[src.x][src.y].timesMoved += 1
        self.logMoves(src, dest)
        # self.positions[dest.x][dest.y] = copy.deepcopy(self.positions[src.x][src.y])
        self.positions[dest.x][dest.y] = self.positions[src.x][src.y].createNewCopy()
        self.positions[src.x][src.y].pieceType = ""
        self.positions[src.x][src.y].pieceColor = ""
        self.positions[src.x][src.y].timesMoved = 0
    
    def revertMove(self, src, dest):

        lastMovements = self.movesLog.pop()
        # pieceEliminated = lastMovements.pop()
        pieceEliminated = lastMovements[1]
        # pieceMoved = lastMovements.pop()
        pieceMoved = lastMovements[0]

        # self.positions[dest.x][dest.y] = copy.deepcopy(pieceEliminated)
        # self.positions[dest.x][dest.y] = pieceEliminated.createNewCopy()
        self.positions[dest.x][dest.y] = pieceEliminated
        # self.positions[src.x][src.y] = copy.deepcopy(pieceMoved)
        # self.positions[src.x][src.y] = pieceMoved.createNewCopy()
        self.positions[src.x][src.y] = pieceMoved
        self.positions[src.x][src.y].timesMoved -= 1