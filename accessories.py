# from pygame import mixer
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
PURPLE = '\033[95m'

class Accessories:

    def __init__(self):
        self.pieceValue = {
            "pawn" : 1,
            "knight" : 3,
            "bishop" : 3,
            "rook" : 5,
            "queen" : 9,
            "king" : 100
        }
        # mixer.init()
        # mixer.music.load(".\\mixkit-confirmation-tone-2867.wav")
        # mixer.music.set_volume(0.7)
        
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
            case "p":
                print(PURPLE + text + RESET, end = "")
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
        for _ in range(n):
            print(" ", end = "")

    def playSound(self):
        # mixer.music.play()
        pass
    
    def print_and_update(self, text, lenInitial, color = 'w'):
        if (color.lower() == 'w'):
            print("\r" + " " * lenInitial + "\r" + text, end='', flush=True)
        else:
            match color.lower():
                case "r":
                    print(RED + "\r" + " " * lenInitial + "\r" + text + RESET, end = "", flush = True)
                case "g":
                    print(GREEN + "\r" + " " * lenInitial + "\r" + text + RESET, end = "", flush = True)
                case "y":
                    print(YELLOW + "\r" + " " * lenInitial + "\r" + text + RESET, end = "", flush = True)
                case "b":
                    print(BLUE + "\r" + " " * lenInitial + "\r" + text + RESET, end = "", flush = True)
                case "p":
                    print(PURPLE + "\r" + " " * lenInitial + "\r" + text + RESET, end = "", flush = True)