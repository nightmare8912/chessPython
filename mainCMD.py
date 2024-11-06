import play as pl

class MainCMD:
    
    def start(self):

        play = pl.Play()
        opt = -1
        opt = int(input("Enter 1 to play with friend, 2 to play with computer, 3 for computer vs computer: "))
        match opt:
            case 1:
                play.humanPlaysHuman()
            
            case 2:
                play.humanPlaysComputer()

            case 3:
                play.computerPlaysComputer()
