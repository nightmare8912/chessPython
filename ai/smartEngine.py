import board as bd
import movements as mv
import coordinates
import accessories as acs
import evaluator as ev

class SmartEngine:

    def __init__(self, board, movements, engColor, intelligence):
        self.board = board
        self.movements = movements
        self.engColor = engColor
        self.intelligence = intelligence
        self.accs = acs.Accessories()
        self.evaluator = ev.Evaluator(self.board)

    def getAllMoves(self, color):
        
        allMoves = []
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPiceAt(coord).pieceColor == color):
                    allMoves.append(self.movements.getPossibleMoves(coord))
        return allMoves
    
    def getOppositeColor(self, color):
       
        if (color == "white"):
            return "black"
        else:
            return "white"
    
    def makeSelection(self, moves):
        for i in moves:
            pass
    