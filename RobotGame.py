
def RobotGameSpg(): # Defenition for the robot game

    print("\nVelkommen til robot spillet \nDer vil være 3 opgaver, som giver 1 point for hvert rigtigt svar, og ved forkert svar vil der blive trukket 1 point fra.") # Welcome sentence

    PlayRobot = 0 # Init of PlayRobot

    PointRobot = 0

    NumbSpg = 1 # Init of NumbSpg

    EndRobotGame = 0 # Init of PointRobot

    while NumbSpg < 4: # While loop for the questions robot game, only active when the numbspg is under 4. 
        #If the answer is right then add 1 point to the score, and if the answer is wrong then minus 1 point to the score

        PlayRobot = input(str("\nFor at komme igang med robot spillet tryk 1, for at stoppe tryk 0: ")) # Input choice

        if PlayRobot == "0": # Stops the loop when the input is 0
            break

        elif PlayRobot == "1": # Starts the questions if the input is 1
            while NumbSpg == 1: # When NumbSpg is equal to 1 and then starts the questions 
                print("\nSpørgsmål 1:") # The next 2 prints is just to print information about question 1 
                print("De følgende koordinater (40;50;60) - (x;y;z) - koordinatorne er i cm. Disse koordinatorne er robottens home position. \nNu skal robottens position rykkes 20 cm op af z-aksen ud fra home positionen")
                if input(str("Indtast det rigtige svar: ")).lower() == "(40;50;80)": # Input the right answer
                    PointRobot += 1 # If the answer is right then add 1 point to robot point
                    NumbSpg += 1 # Go to next question 
                else:
                    PointRobot -= 1 # If the answer is wrong the minus 1 in robot point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointRobot)
                print(NumbSpg)

            while NumbSpg == 2: # When NumbSpg is equal to 1 and then starts the questions 
                print("\nSpørgsmål 2:") # The next 2 prints is just to print information about question 2
                print("De følgende koordinater (40;50;80) - (x;y;z) - koordinatorne er i cm. Disse koordinatorne er robottens home position. \nNu skal home positionen rykkes 1000 mm hen af x-aksen, her kommer 4 valgmuligheder")
                print("a: (120;150;180)\nb: (140;50;80)\nc: (1040;1250;1880)\nd: (10040;-1050;-5080)")
                if input(str("Indtast det rigtige svar: ")).lower() == "b": # Input the right answer
                    PointRobot += 1 # If the answer is right then add 1 point to robot point
                    NumbSpg += 1 # Go to next question 
                else:
                    PointRobot -= 1 # If the answer is wrong the minus 1 in robot point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointRobot)
                print(NumbSpg)
            
            while NumbSpg == 3: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 3:") # The next 2 prints is just to print information about question 3
                print("De følgende koordinater (140;50;80) - (x;y;z) - koordinatorne er i cm. Disse koordinatorne er robottens home position. \nNu skal home positionen rykkes 1 mm hen af y-aksen, her kommer 4 valgmuligheder")
                print("a: (10.5;50;80)\nb: (140.99;50.25;80)\nc: (100;10;1)\nd: (140.1;50;80)")
                if input(str("Indtast det rigtige svar: ")).lower() == "d": # Input the right answer
                    PointRobot += 1 # If the answer is right then add 1 point to robot point
                    NumbSpg += 1 # Go to next question 
                    print("Svaret er rigtigt, du går videre til næste spørgsmål")
                else:
                    PointRobot -= 1 # If the answer is wrong the minus 1 in robot point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointRobot)
                print(NumbSpg)
    
    return PointRobot