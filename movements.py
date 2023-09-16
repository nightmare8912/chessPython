import pieces
import copy
import math
import time
import board as bd
import accessories
import coordinates

class Movements:

    def __init__(self, board):
        self.coord = coordinates.Coordinates(-1, -1)
        self.acs = accessories.Accessories()
        self.board = board

    def getAllPossibleMoves(self, src):
        # all possible moves with that piece, but check is not considered
        allMovesWithCheck = []

        if (self.board.getPieceAt(src).pieceType == "pawn"):
            allMovesWithCheck = self.pawnMovements(src)
        elif (self.board.getPieceAt(src).pieceType == "rook"):
            allMovesWithCheck = self.rookMovements(src)
        elif (self.board.getPieceAt(src).pieceType == "knight"):
            allMovesWithCheck = self.knightMovements(src)
        elif (self.board.getPieceAt(src).pieceType == "bishop"):
            allMovesWithCheck = self.bishopMovements(src)
        elif (self.board.getPieceAt(src).pieceType == "king"):
            allMovesWithCheck = self.kingMovements(src)
        elif (self.board.getPieceAt(src).pieceType == "queen"):
            allMovesWithCheck = self.queenMovements(src)
        else:
            print("match not found, as piecetype = ", self.board.getPieceAt(src).pieceType)
        
        return allMovesWithCheck

    def getPossibleMoves(self, src):
        # all possible moves with that piece, but check is not considered
        allMovesWithoutCheck = self.getAllPossibleMoves(src)

        if len(allMovesWithoutCheck) == 0:
            return []

        # all moves considered for that piece including check(as of now both are same, will add check feature in future)
        allMovesWithCheck = []
        for move in allMovesWithoutCheck:
            if (self.isMovementPossibleConsideringOnlyCheckAndIntersections(src, move)):
                allMovesWithCheck.append(move)
        return allMovesWithCheck

    def isMovementPossibleConsideringOnlyCheckAndIntersections(self, src, dest):

        if (not dest.isValid()):
            return False
        
        color = self.board.getPieceAt(src).pieceColor
        self.board.movePiece(src, dest)

        if (self.isCheck(self.getKingsLocn(color))):
            self.board.revertMove(src, dest)
            return False
        self.board.revertMove(src, dest)
        return True

    def isOccupied(self, toCheck):      
        return (self.board.getPieceAt(toCheck).pieceColor != "")

    def pawnMovements(self, src):
        
        colorFactor = 1
        coord = coordinates.Coordinates(-1, -1)
        possibleMoves = []

        if (self.board.getPieceAt(src).pieceColor == "black"):
            colorFactor = -1

        coord.assignValue(src.x - colorFactor, src.y)

        if (coord.isValid() and not self.isOccupied(coord)):
            possibleMoves.append(coord.createNewCopy())

        if (coord.isValid() and not self.isOccupied(coord)):
            coord.assignValue(src.x - (colorFactor * 2), src.y)
            if (coord.isValid() and not self.isOccupied(coord) and self.board.getPieceAt(src).timesMoved == 0):
                possibleMoves.append(coord.createNewCopy())
        
        coord.assignValue(src.x - colorFactor, src.y - 1)
        if (coord.isValid() and self.isOccupied(coord) and self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
            possibleMoves.append(coord.createNewCopy())
        
        coord.assignValue(src.x - colorFactor, src.y + 1)
        if (coord.isValid() and self.isOccupied(coord) and self.board.getPieceAt(coord).pieceColor != self.board.getPieceAt(src).pieceColor):
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
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 1
        j = src.y + 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 1
        j = src.y - 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x + 1
        j = src.y - 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x + 2
        j = src.y + 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 2
        j = src.y + 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x - 2
        j = src.y - 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x + 2
        j = src.y - 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != self.board.getPieceAt(src).pieceColor):
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
                if (self.board.getPieceAt(coord).pieceColor == "" or (self.board.getPieceAt(coord).pieceColor == self.board.getPieceAt(pos).pieceColor)):
                    continue
                possibleMoves = self.getAllPossibleMoves(coord)
                for k in possibleMoves:
                    if ((k.x == pos.x) and (k.y == pos.y)):
                        threatsFrom.append(coord.createNewCopy())
        return threatsFrom


    def getKingsLocn(self, color):
        for i in range(8):
            for j in range(8):
                if (self.board.positions[i][j].pieceColor == color and self.board.positions[i][j].pieceType == "king"):
                    return coordinates.Coordinates(i, j)
        return coordinates.Coordinates(-1, -1)

    def isCheck(self, kingPos):
        return (len(self.getThreatsAt(kingPos)) != 0)
        
