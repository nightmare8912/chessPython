import pygame as p
import ChessLogics

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAXFPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessLogics.GameState()
    loadImages()
    running = True
    sqSelected = () # no square is selected, keeps track of the last click of the user : tuple(row, col)
    playerClicks = []# keep track of player clicks (two tuples: [(6, 4), (4, 4)])
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
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []
        drawGameState(screen, gs)
        clock.tick(15)
        p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if (piece != "--"):
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# if __name__ == "__main__":
#     main()

