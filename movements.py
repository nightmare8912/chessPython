import math
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
        move_functions = {
            "pawn": self.pawnMovements,
            "rook": self.rookMovements,
            "knight": self.knightMovements,
            "bishop": self.bishopMovements,
            "king": self.kingMovements,
            "queen": self.queenMovements,
        }

        piece = self.board.getPieceAt(src)
        allMovesWithCheck = move_functions.get(piece.pieceType, lambda x: [])(src)
        return allMovesWithCheck

    def getPossibleMoves(self, src):
        # all possible moves with that piece, but check is not considered
        allMovesWithoutCheck = self.getAllPossibleMoves(src)

        if len(allMovesWithoutCheck) == 0:
            return []

        # all moves considered for that piece including check
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
        pieceAtSrc = self.board.getPieceAt(src)
        if (pieceAtSrc.pieceColor == "black"):
            colorFactor = -1

        coord.assignValue(src.x - colorFactor, src.y)

        if (coord.isValid() and not self.isOccupied(coord)):
            possibleMoves.append(coord.createNewCopy())

        if (coord.isValid() and not self.isOccupied(coord)):
            coord.assignValue(src.x - (colorFactor * 2), src.y)
            if (coord.isValid() and not self.isOccupied(coord) and pieceAtSrc.timesMoved == 0):
                possibleMoves.append(coord.createNewCopy())
        
        coord.assignValue(src.x - colorFactor, src.y - 1)
        if (coord.isValid() and self.isOccupied(coord) and self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
            possibleMoves.append(coord.createNewCopy())
        
        coord.assignValue(src.x - colorFactor, src.y + 1)
        if (coord.isValid() and self.isOccupied(coord) and self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
            possibleMoves.append(coord.createNewCopy())
        
        return possibleMoves

    def rookMovements(self, src):

        coord = coordinates.Coordinates(-1, -1)
        pieceAtSrc = self.board.getPieceAt(src)
        possibleMoves = []

        i = src.x + 1
        j = src.y

        while (i <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i += 1

        i = src.x - 1
        j = src.y

        while (i >= 0):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            i -= 1

        i = src.x
        j = src.y + 1

        while (j <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            j += 1

        i = src.x
        j = src.y - 1

        while (j >= 0):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
                    possibleMoves.append(coord.createNewCopy())
                break
            possibleMoves.append(coord.createNewCopy())
            j -= 1
        
        return possibleMoves

    def knightMovements(self, src):
        coord = coordinates.Coordinates(-1, -1)
        pieceAtSrc = self.board.getPieceAt(src)
        possibleMoves = []

        i = src.x + 1
        j = src.y + 2
        coord.assignValue(i, j)
        
        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x - 1
        j = src.y + 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 1
        j = src.y - 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x + 1
        j = src.y - 2
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x + 2
        j = src.y + 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())


        i = src.x - 2
        j = src.y + 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x - 2
        j = src.y - 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())

        i = src.x + 2
        j = src.y - 1
        coord.assignValue(i, j)

        if coord.isValid():
            if (self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor  != pieceAtSrc.pieceColor):
                possibleMoves.append(coord.createNewCopy())

        return possibleMoves

    def bishopMovements(self, src):
        coord = coordinates.Coordinates(-1, -1)
        pieceAtSrc = self.board.getPieceAt(src)
        possibleMoves = []

        i = src.x + 1
        j = src.y + 1
    
        while(i <= 7 and j <= 7):
            coord.assignValue(i, j)
            if (self.isOccupied(coord)):
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
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
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
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
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
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
                if (self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor):
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
        pieceAtSrc = self.board.getPieceAt(src)
        possibleMoves = []

        # Define the relative movements for a king
        moves = [
            (1, 0), (1, 1), (0, 1), (-1, 1),
            (-1, 0), (-1, -1), (0, -1), (1, -1)
        ]

        for move in moves:
            i = src.x + move[0]
            j = src.y + move[1]
            coord.assignValue(i, j)

            if coord.isValid():
                if self.isOccupied(coord) == False or self.board.getPieceAt(coord).pieceColor != pieceAtSrc.pieceColor:
                    possibleMoves.append(coord.createNewCopy())

        return possibleMoves


    # def getThreatsAt(self, pos):

    #     threatsFrom = []
    #     coord = coordinates.Coordinates(-1, -1)
    #     for i in range(8):
    #         for j in range(8):
    #             coord.assignValue(i, j) 
    #             if (self.board.getPieceAt(coord).pieceColor == "" or (self.board.getPieceAt(coord).pieceColor == self.board.getPieceAt(pos).pieceColor)):
    #                 continue
    #             possibleMoves = self.getAllPossibleMoves(coord)
    #             for k in possibleMoves:
    #                 if ((k.x == pos.x) and (k.y == pos.y)):
    #                     threatsFrom.append(coord.createNewCopy())
    #     return threatsFrom

    def getKingsLocn(self, color):
        for i in range(8):
            for j in range(8):
                if (self.board.positions[i][j].pieceColor == color and self.board.positions[i][j].pieceType == "king"):
                    return coordinates.Coordinates(i, j)
        return coordinates.Coordinates(-1, -1)

    def isCheck(self, kingPos):
        # return (len(self.getThreatsAt(kingPos)) != 0)
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8):
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == "" or (self.board.getPieceAt(coord).pieceColor == self.board.getPieceAt(kingPos).pieceColor)):
                    continue
                possibleMoves = self.getAllPossibleMoves(coord)
                for k in possibleMoves:
                    if ((k.x == kingPos.x) and (k.y == kingPos.y)):
                        return True
        return False
        
    def getValidCastlingMoves(self, src):

        castlingLocn = self.getAllCastlingMoves(self.board.getPieceAt(src).pieceColor)
        tempValidMoves = []
        for dest in castlingLocn:
            if (self.board.getPieceAt(dest).pieceType != "rook"):
                continue
            if (self.board.getPieceAt(src).pieceColor != self.board.getPieceAt(dest).pieceColor):
                continue
            if (self.board.getPieceAt(src).timesMoved != 0 and self.board.getPieceAt(dest).timesMoved != 0):
                continue
            if (self.isCheck(src)):
                continue
            tempValidMoves.append(dest.createNewCopy())
        
        validContenders = []
        colorFactor = 0
        if (self.board.getPieceAt(src).pieceColor == "white"):
            colorFactor = 7
        coord1 = coordinates.Coordinates(colorFactor, 3)
        coord2 = coordinates.Coordinates(colorFactor, 5)
        for dest in tempValidMoves:
            allMovesForPieceAtDest = self.getPossibleMoves(dest)
            for move in allMovesForPieceAtDest:
                if move.compare(coord1) and self.board.getPieceAt(coord1).pieceType == "":
                    validContenders.append(move)
                if move.compare(coord2) and self.board.getPieceAt(coord1).pieceType == "":
                    validContenders.append(move)

        return validContenders
                
    
    def getAllCastlingMoves(self, color):
        colorFactor = 0
        if (color == "white"):
            colorFactor = 7
        dest1 = coordinates.Coordinates(-1, -1)
        dest2 = coordinates.Coordinates(-1, -1)
        dest1.assignValue(colorFactor, 0)
        dest2.assignValue(colorFactor, 7)

        return [dest1, dest2]
    
    def isMate(self, color):
        allPossibleMoves = []
        coord = coordinates.Coordinates(-1, -1)
        for i in range(8):
            for j in range(8): 
                coord.assignValue(i, j)
                if (self.board.getPieceAt(coord).pieceColor == color):
                    if (len(self.getPossibleMoves(coord)) != 0):
                        return False
        return True