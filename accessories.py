RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class Accessories:

    def __init__(self):
        self.pieceValue = {
            "pawn" : 1,
            "knight" : 3,
            "bishop" : 3,
            "rook" : 5,
            "queen" : 9,
            "king" : 1000
        }
        
    def printInColor(self, text, color):
        match color.lower():
            case "r":
                print(RED + text + RESET, end = "")
            case "g":
                print(GREEN + text + RESET, end = "")
            case "y":
                print(YELLOW + text + RESET, end = "")
            case "b":
                print(BLUE + text + RESET, end = "")
    def printSL(self, text, sep, end = ""):
        print(text, sep, end)
    
    def mapXCoordsToChessXCoords(self, x):
        chessXCoords = ""
        mapXCords = {char: index for index, char in enumerate('abcdefgh', start=1)}
        chessXCoords += str(mapXCords[x])
        return chessXCoords
    
    def mapYCoordsToChessYCoords(self, y):
        chessYCoords = ""
        mapYCords = {i : 8 - i for i in range(8)}
        chessYCoords += str(mapYCords[y])

        return chessYCoords

    def mapCoordsToChessCoords(self, x, y):
        # chessCoords = ""
        # mapXCords = {char: index for index, char in enumerate('abcdefgh', start=1)}
        # mapYCords = {8-i:i for i in range(8)}
        # chessCoords += mapYCords[coord.y]
        # chessCord += mapXCords[coord.x]

        return self.mapXCoordsToChessXCoords(x) + self.mapYCoordsToChessYCoords(y)

    def getPieceWeightage(self, piece):
        return self.pieceValue[piece]
    
    def printSpaces(self, n):
        for i in range(n):
            print(" ", end = "")