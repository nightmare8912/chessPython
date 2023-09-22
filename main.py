import mainCMD as cmd
import mainGUI as gui
import accessories as acs

accs = acs.Accessories()

print("welcome to this chess game! here's a quick walkthrough of the game")
print("You can play the game in two modes, CMD and GUI(gui is not completed yet, so it will give and error)", end = "")
print("After this, you can play this game with either your friend or the computer", end = "")
print("To play with computer, you have to choose a level, ", end = "")
accs.printInColor("(recommended value is 3)", 'y')
print(", though potentially you can chose any value of your liking, but a level 4 bot can take", end = "")
print("upto half an hour to make a move, and a level 2 bot will just be very weak", end ="")
print("I am currently working on more efficient algorithms so that the bot level can be increased to atleast 4", end = "")

print("\nWhile moving a piece, first you need to chose its coordinates as x and y", end = "")
accs.printInColor("(x being horizontal and y being vertical)", 'y')
print("After selecting the piece you want to move, you will be shown the possible moves for that piece on the board", end = "")
print("You then need to enter the x and y coordinates of the location where you want to take the piece\n")

accs.printInColor("\nPlease keep in mind that moves like castling and en-passant are not included in this game, and will be added in future!\n", "r")
accs.printInColor("\nHappy Playing!\n", 'g')


opt = int(input("Enter 1 to play in GUI, 2 to play in CMD: "))
match opt:
    case 1:
        gu = gui.MainGUI()
        gu.start()
    case 2:
        cm = cmd.MainCMD()
        cm.start()