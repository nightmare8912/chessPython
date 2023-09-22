import mainCMD as cmd
import mainGUI as gui
import accessories as acs

accs = acs.Accessories()

accs.printInColor("\n\n\nwelcome to this chess game! here's a quick walkthrough of the game!!\n\n".upper(), 'g')
print("You can play the game in two modes, CMD and GUI(gui is not completed yet, so it will give an error). \n", end = "")
print("Also, you can play this game with either your friend or the computer. ", end = "")
print("To play with computer, you\nhave to choose a level, ", end = "")
accs.printInColor("(recommended value is 3)", 'y')
print(", though potentially you can chose any value of your\nliking, but a level 4 bot can take", end = "")
print(" upto half an hour to make a move, and a level 2 bot will just be\nvery weak. ", end ="")
print("The engine at level 3 is still slow and can take maximum of 95 - 100 seconds to  make a move.\n", end ="")
print("As the game proceeds and the possible moves increase, the engine will take longer. ", end ="")
print("The engine will be\nfastest at the end of the game, slowest at the middle and moderate at start ", end ="")
print(". I am currently working on\nmore efficient algorithms so that the bot level can be increased to atleast 4.", end = "")

print("\n\nWhen moving a piece, you first need to chose its coordinates as x and y", end = "")
accs.printInColor(" (x being horizontal and y being\nvertical). ", 'y')
print("After selecting the piece you want to move, you will be shown the possible moves for that piece\non the board. ", end = "")
print("You then need to enter the x and y coordinates of the location where you want to take the piece\n")

accs.printInColor("\nPlease do note that moves like castling and en-passant are not included in this game, and will be added\nin the future!\n", "r")
accs.printInColor("\nHappy Playing!\n", 'g')


# opt = int(input("Enter 1 to play in GUI, 2 to play in CMD: "))
opt = 2
match opt:
    case 1:
        gu = gui.MainGUI()
        gu.start()
    case 2:
        cm = cmd.MainCMD()
        cm.start()