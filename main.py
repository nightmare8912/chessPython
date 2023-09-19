import mainCMD as cmd
import mainGUI as gui

# opt = int(input("Enter 1 to play in GUI, 2 to play in CMD: "))
opt = 1
match opt:
    case 1:
        gu = gui.MainGUI()
        gu.start()
    case 2:
        cm = cmd.MainCMD()
        cm.start()