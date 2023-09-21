import pygame as p
from gui import ChessLogics
import playGUIBackend as pl
import coordinates

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAXFPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


class PlayGUI:       

    def humanPlaysHuman(self):
        p.init()
        screen = p.display.set_mode((WIDTH, HEIGHT))
        clock = p.time.Clock()
        screen.fill(p.Color("white"))
        gs = ChessLogics.GameState()
        loadImages()
        coord = coordinates.Coordinates(-1, -1)
        play = pl.Play()
        running = True
        sqSelected = () # no square is selected, keeps track of the last click of the user : tuple(row, col)
        playerClicks = []# keep track of player clicks (two tuples: [(6, 4), (4, 4)])
        print("images were loaded")
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos() # x, y locn
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    print(row, col, sep = ", ")
                    if (sqSelected == (row, col)): #user clicked same square two times, i.e., we will reset
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if (len(playerClicks) == 2): # user wants to move
                        move = ChessLogics.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        src, dest = self.convertMoveToCoordinates(playerClicks)
                        if (play.humanPlaysHuman(src, dest)):
                            gs.makeMove(move)
                        else:
                            sqSelected = ()
                            playerClicks = []
                            continue
                        sqSelected = ()
                        playerClicks = []
            coord.assignValue(playerClicks[0][0], playerClicks[0][1])
            allMoves = play.returnPossibleMoves(coord)
            self.drawGameState(screen, gs, allMoves, sqSelected)
            clock.tick(15)
            p.display.flip()

    def humanPlaysComputer(self):
        pass
    def computerPlaysComputer(self):
        pass

    def drawGameState(self, screen, gs, validMoves, sqSelected):
        self.drawBoard(screen)
        allMoves = []
        for moves in validMoves:
            allMoves.append
        self.highlightSquares(screen, gs, validMoves, sqSelected)
        self.drawPieces(screen, gs.board)

    def drawBoard(self, screen):
        colors = [p.Color("white"), p.Color("gray")]
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                color = colors[((r + c) % 2)]
                p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawPieces(self, screen, board):
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = board[r][c]
                if (piece != ""):
                    screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def convertMoveToCoordinates(self, move):
        src = coordinates.Coordinates(-1, -1)
        dest = coordinates.Coordinates(-1, -1)
        print("move = ", move)
        src.x = move[0][0]
        src.y = move[0][1]
        dest.x = move[1][0]
        dest.y = move[1][1]
        src.printCoordinates()
        dest.printCoordinates()
        return src, dest
    
    def highlightSquares(self, screen, gs, validMoves, sqSelected):
        if (sqSelected != ()):
            r, c = sqSelected
            # to highlight selected square
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100) # transparency
            s.fill(p.Color('blue'))
            screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
            # highlight possible moves from that square
            s.fill(p.Color("yellow"))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol * SQ_SIZE, move.endRow *SQ_SIZE))