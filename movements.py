import pieces
import copy
import math
import board as bd
import accessories
import coordinates

class Movements:

    def __init__(self):
        self.coord = coordinates.Coordinates(-1, -1)
        pass
    
    def updateBoard(self, board):
        self.board = board

    def getPossibleMoves(self, board, src):
        # all possible moves with that piece, but check is not considered
        allMovesWithoutCheck = []

        if (board.getPieceAt(src).pieceType == "pawn"):
            allMovesWithoutCheck = self.pawnMovements(src)
        elif (board.getPieceAt(src).pieceType == "rook"):
            allMovesWithoutCheck = self.rookMovements(src)
        elif (board.getPieceAt(src).pieceType == "knight"):
            allMovesWithoutCheck = self.knightMovements(src)
        elif (board.getPieceAt(src).pieceType == "bishop"):
            allMovesWithoutCheck = self.bishopMovements(src)
        elif (board.getPieceAt(src).pieceType == "king"):
            allMovesWithoutCheck = self.kingMovements(src)
        elif (board.getPieceAt(src).pieceType == "queen"):
            allMovesWithoutCheck = self.queenMovements(src)
        
        if allMovesWithoutCheck is None:
            return []

        # all moves considered for that piece including check(as of now both are same, will add check feature in future)
        allMovesWithCheck = []

        for move in allMovesWithoutCheck:
            if (self.isMovementPossible(src, move)):
                allMovesWithCheck.append(move)
        return allMovesWithCheck

    def isMovementPossible(self, src, dest):

        # dest.printCoordinates(dest)
        if (not dest.isValid()):
            return False
        # board = copy.deepcopy(self.board)
        self.board.movePiece(src, dest)

        if (self.isCheck(self.getKingsLocn(self.board.getPieceAt(src).pieceColor))):
            return False
        return True

    def isOccupied(self, toCheck):   
        if (not toCheck.isValid()):
            return False     
        return (self.board.getPieceAt(toCheck).pieceColor != "")

    def pawnMovements(self, src):
        
        colorFactor = 1
        coord = coordinates.Coordinates(-1, -1)
        possibleMoves = []

        # print("piece color: ", self.board.getPieceAt(src).pieceColor)
        if (self.board.getPieceAt(src).pieceColor == "black"):
            colorFactor = -1

        coord.assignValue(src.x - colorFactor, src.y)

        if (not self.isOccupied(coord)):
            possibleMoves.append(coord.createNewCopy())
            
        for i in possibleMoves:
            i.printCoordinates(i)
        print()

        if (not self.isOccupied(coord)):
            coord.assignValue(src.x - (colorFactor * 2), src.y)
            if (not self.isOccupied(coord) and self.board.getPieceAt(src).timesMoved == 0):
                possibleMoves.append(coord.createNewCopy())

        for i in possibleMoves:
            i.printCoordinates(i)
        print()
        
        coord.assignValue(src.x - colorFactor, src.y - 1)
        if (self.isOccupied(coord) and self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
            possibleMoves.append(coord.createNewCopy())
        
        for i in possibleMoves:
            i.printCoordinates(i)
        print()
        
        coord.assignValue(src.x - 1, src.y + 1)
        if (self.isOccupied(coord) and self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
            possibleMoves.append(coord.createNewCopy())
        
        return possibleMoves

    def rookMovements(self, src):

        coord = coordinates.Coordinates(-1, -1)
        possibleMoves = []

        i = src.x + 1
        j = src.y

        while (i <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i += 1

        i = src.x - 1
        j = src.y

        while (i >= 0):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i -= 1

        i = src.x
        j = src.y + 1

        while (j <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            j += 1

        i = src.x
        j = src.y - 1

        while (j >= 0):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            j -= 1
        
        return possibleMoves

    def knightMovements(self, src):
        coord = coordinates.Coordinates(-1, -1)
        possibleMoves = []

        i = src.x + 1
        j = src.y + 2
        coord.assignValue(i, j)
        
        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 1
        j = src.y + 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 1
        j = src.y - 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x + 1
        j = src.y - 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x + 2
        j = src.y + 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 2
        j = src.y + 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x - 2
        j = src.y - 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x + 2
        j = src.y - 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(coord).pieceColor):
                possibleMoves.append(coord.createNewCopy())

        return possibleMoves

    def bishopMovements(self, src):
        coord = coordinates.Coordinates(-1, -1)
        possibleMoves = []

        i = src.x + 1
        j = src.y + 1
    
        while(i <= 7 and j <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i += 1
            j += 1
        
        i = src.x - 1
        j = src.y + 1
        
        while(i >= 0 and j <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i -= 1
            j += 1
   
        i = src.x - 1
        j = src.y - 1
        
        while(i >= 0 and j >= 0):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i -= 1
            j -= 1

        i = src.x + 1
        j = src.y - 1
        

        while(i <= 7 and j >= 0):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i += 1
            j -= 1
        
        return possibleMoves

    def queenMovements(self, src):
        possibleMoves = []

        possibleMoves = self.rookMovements(src)
        possibleMoves.extend(self.bishopMovements(src))

        return possibleMoves

    def kingMovements(self, src):
        coord = coordinates.Coordinates(-1, -1)
        possibleMoves = []
        queensMove = self.queenMovements(src)

        for i in queensMove:
            if (i.getDistance(src, i) == 1 or i.getDistance(src, i) == math.sqrt(2)):
                possibleMoves.append(i.createNewCopy())
        return possibleMoves

    def getThreatsAt(self, pos):

        threatsFrom = []
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                self.getPossibleMoves(self.board, coord)

                if (pos in self.getPossibleMoves(self.board, coord)):
                    threatsFrom.append(coord.createNewCopy())
        return threatsFrom


    def getKingsLocn(self, color):
        for i in range(8):
            for j in range(8):
                if (self.board.positions[i][j].pieceColor == color):
                    return coordinates.Coordinates(i, j)
        return None

    def isCheck(self, kingPos):
        return self.getThreatsAt(kingPos) is not None
        
