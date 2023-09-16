import play as pl

play = pl.Play()

opt = 2
# opt = int(input("Enter 1 to play with friend, 2 to play with computer: "))
match opt:
    case 1:
        play.startPlayingHuman()
    
    case 2:
        play.startPlayingComputer()

