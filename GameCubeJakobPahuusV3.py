
print("---Velkommen til Jakobs spil---") # Prints a welcome message

import WriteHighScore

Progress = 0 # Init of the progress variabel

PointScore = 0

while True: # loop where the player can choose what to see  

    # These 3 prints functions under here makes the oppertunities visible for the player
    print("Start nyt spil - Tryk S")
    print("Tidligere spil - Tryk L")
    print("Se highscore - Tryk H")

    StartDecision = str(input("Skriv det ønskede bogstav eller 0 for at stoppe spil")).upper() # Input to choose what to do and the last .upper() is used to make all the character in uppercase 

    # Stop game when the input is equal to 0
    if StartDecision == "0":
        print("Spil stoppet")
        break

    # Save and stops game when input is S
    #elif SaveGame == "SAVE":
     #   break

    # Import of highscore file
    if StartDecision == "H":
        print("highscore")
        import HighScore
        HighScore.HighScoreFile()
        #HighScore.main()
        #import HighScore1
    
    # Start game and make a user
    if StartDecision == "S": 
        print("start")
        print("Opret nu en ny bruger - Tryk U \nLoad tidligere spil - Tryk L")
        StartDecision = input("Skriv det ønskede bogstav").upper()
        
        if StartDecision == "U":
            #import User
            #User.NewUser()
            UserNameTemp = str(input("Write user name: "))
              
            # Import of robot game file
            if Progress == 0:
                import RobotGame
                #RobotGame.RobotGameSpg()
                PointScore += RobotGame.RobotGameSpg()
                Progress += 1
                print(Progress)
                print(PointScore)
                
        
            # Import of PLC game file
            if Progress == 1:
                import PLCGame
                PointScore += PLCGame.PLCGameSpg()
                Progress += 1
                print(Progress)
                print(PointScore)
        
            # Import of Python game file
            if Progress == 2:
                import PythonGame
                PointScore += PythonGame.PythonGameSpg()
                Progress += 1
                print(Progress)
                print(PointScore)

            # Import of ST game file
            if Progress == 3:
                import STGame
                PointScore += STGame.STGameSpg()
                Progress += 1
                print(Progress)
                print(PointScore)

                if Progress == 4 and PointScore < 5:
                    print("Du har for mange forkerte svar, prøv igen")
                    WriteHighScore.NewUser(UserNameTemp, str(PointScore))

            elif Progress == 4 and StartDecision != "0" and point >= 5:
                print("--- Du har nu gennemført spille med en score på ", pointscore, " ---")
                WriteHighScore.NewUser(UserNameTemp, str(PointScore))
                break

    elif StartDecision == "L":
        print("Load")
    
    # If there not is af valid letter typed in
    else:
        print("Forkert bogstav, prøv igen.")

