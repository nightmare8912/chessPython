import board as bd
import movements as mv
import coordinates
import accessories
from ai import engine as eng
from ai import evaluator as ev
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

    def humanPlaysHuman(self):
        
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)
        while(True):
            self.board.drawBoard(self.turn)
            if (self.movements.isMate(self.turn)):
                print()
                self.accs.printInColor("\nThe game is over and " + self.getOppositeTurn(self.turn) + " has won!!\n", "g")
                print()
                break
            print("\n\nIts ", self.turn, "'s turn to move")
            self.accs.printInColor("Current score is: " + str(self.evaluator.evaluateBoard()) + "\n", "b")
            try:
                src.y = int(input("Enter x pos of piece to move: "))
                src.x = int(input("Enter y pos of piece to move: "))
            except:
                self.accs.printInColor("Enter valid value", 'r')
                continue
            if (not src.isValid()):
                    self.accs.printInColor("Enter a valid move!", "r")
                    continue
            possibleMoves = self.movements.getPossibleMoves(src)

            self.board.drawBoardWithMoves(self.turn, possibleMoves)
            
            print("Possible moves: ")
            for i in possibleMoves:
                i.printCoordinates()
            print()
            print("You want to move ", self.board.positions[src.x][src.y].pieceType, " of color ", self.board.getPieceAt(src).pieceColor)
            try:
                dest.y = int(input("Enter x pos of where you want to to move(-1 to change piece): "))
                if (dest.y == -1):
                    continue
            except:
                self.accs.printInColor("Enter valid value", 'r')
                continue
            try:
                dest.x = int(input("Enter y pos of where you want to to move(-1 to change piece): "))
                if (dest.x == -1):
                    continue
            except:
                self.accs.printInColor("Enter valid value", 'r')
                continue
            if (not dest.isValid()):
                    self.accs.printInColor("Enter a valid move!", "r")
                    continue
            if (self.validateMove(src, dest)):
                self.printMovement(src, dest)
                self.board.movePiece(src, dest)
            else:
                self.accs.printInColor(self.error, 'r')
                continue
            self.turn = self.getOppositeTurn(self.turn)
        
    def humanPlaysComputer(self):

        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)

        selectedColor = input("Please enter your color (White for white, Black for black(not case sensitive)): ").lower()
        if (selectedColor[0] == 'b'):
            selectedColor = 'black'
        elif (selectedColor[0] == 'w'):
            selectedColor = "white"
        intelligence = int(input("Please enter the intelligence of computer(higher intelligence means higher think time)(recommended -> 3): "))
        dynamicDepthEnabled = input("Enable dynamic depth(allows intelligence to adjust its depth, based on time consumed)?(yes/no): ")
        dynamicDepthEnabled = True if dynamicDepthEnabled[0].lower() == 'y' else False
        self.engine = eng.Engine(self.board, self.movements, self.getOppositeTurn(selectedColor), intelligence, dynamicDepthEnabled)
        while(True):
            self.board.drawBoard(selectedColor)
            if (self.movements.isMate(self.turn)):
                print()
                self.accs.printInColor("\nThe game is over and " + self.getOppositeTurn(self.turn) + " has won!!\n", "g")
                print()
                break
            print("\n\nIts ", self.turn, "'s turn to move\n\n")
            self.accs.printInColor("Current score is: " + str(self.evaluator.evaluateBoard()) + "\n", "b")

            if (self.turn == selectedColor):
                try:
                    src.y = int(input("Enter x pos of piece to move: "))
                    src.x = int(input("Enter y pos of piece to move: "))
                    if (not src.isValid()):
                        self.accs.printInColor("Enter a valid move!", "r")
                        continue
                except:
                    self.accs.printInColor("Enter valid value", 'r')
                    continue
                possibleMoves = self.movements.getPossibleMoves(src)

                self.board.drawBoardWithMoves(self.turn, possibleMoves)
                print("Possible moves: ")
                for i in possibleMoves:
                    i.printCoordinates()
                print()
                print("You want to move ", self.board.positions[src.x][src.y].pieceType, " of color ", self.board.getPieceAt(src).pieceColor)
                try:
                    dest.y = int(input("Enter x pos of where you want to to move(-1 to change piece): "))
                    if (dest.y == -1):
                        continue
                except:
                    self.accs.printInColor("Enter valid value", 'r')
                    continue
                try:
                    dest.x = int(input("Enter y pos of where you want to to move(-1 to change piece): "))
                except:
                    self.accs.printInColor("Enter valid value", 'r')
                    continue
                if (dest.x == -1):
                    continue
                if (not dest.isValid()):
                    self.accs.printInColor("Enter a valid move!", "r")
                    continue
                if (self.validateMove(src, dest)):
                    self.printMovement(src, dest)
                    self.board.movePiece(src, dest)
                else:
                    self.accs.printInColor(self.error, 'r')
                    continue
            else:
                src, dest = self.engine.generateMove()
                self.printMovement(src, dest)
                self.board.movePiece(src, dest)
            self.turn = self.getOppositeTurn(self.turn)

    def computerPlaysComputer(self):
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)
        intelligence1 = int(input("Please enter the intelligence of eng 1(higher intelligence means higher think time)(1-3): "))
        dynamicDepthEnabled1 = input("Enable dynamic depth for eng 1(allows intelligence to adjust its depth, based on time consumed)?(yes/no): ")
        dynamicDepthEnabled1 = True if dynamicDepthEnabled1[0].lower() == 'y' else False
        intelligence2 = int(input("Please enter the intelligence of computer2(higher intelligence means higher think time)(1-3): "))
        dynamicDepthEnabled2 = input("Enable dynamic depth for eng 2(allows intelligence to adjust its depth, based on time consumed)?(yes/no): ")
        dynamicDepthEnabled2 = True if dynamicDepthEnabled2[0].lower() == 'y' else False
        self.engine1 = eng.Engine(self.board, self.movements, "white", intelligence1, dynamicDepthEnabled1)
        self.engine2 = eng.Engine(self.board, self.movements, "black", intelligence2, dynamicDepthEnabled2)
        while(True):
            self.board.drawBoard(self.turn)
            if (self.movements.isMate(self.turn)):
                print()
                self.accs.printInColor("\nThe game is over and " + self.getOppositeTurn(self.turn) + " has won!!\n", "g")
                print()
                break
            print("\n\nIts ", self.turn, "'s turn to move\n\n")
            self.accs.printInColor("Current score is: " + str(self.evaluator.evaluateBoard()) + "\n", "b")

            if (self.turn == "white"):
                src, dest = self.engine1.generateMove()
            else:
                src, dest = self.engine2.generateMove()
            self.printMovement(src, dest)
            self.board.movePiece(src, dest)
            self.turn = self.getOppositeTurn(self.turn)

    def printMovement(self, src, dest):
        print(self.board.getPieceAt(src).pieceColor + "'s "+ self.board.getPieceAt(src).pieceType +" was moved from ", end = "")
        src.printCoordinates()
        print(" to ", end = "")
        dest.printCoordinates()
        print()
