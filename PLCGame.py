
def PLCGameSpg(): # Defenition for the PLC game

    print("\nVelkommen til PLC spillet \nDer vil være 3 opgaver, som giver 1 point for hvert rigtigt svar, og ved forkert svar vil der blive trukket 1 point fra.") # Welcome sentence

    PointPLC = 0 # Init of PointPLC

    PlayPLC = 0 # Init of PlayPLC

    NumbSpg = 1 # Init of NumbSpg

    while NumbSpg < 4: # While loop for the questions PLC game, only active when the numbspg is under 4. 
        #If the answer is right then add 1 point to the score, and if the answer is wrong then minus 1 point to the score

        PlayPLC = input(str("\nFor at komme igang med PLC spillet tryk 1, for at stoppe tryk 0: ")) # Input choice

        if PlayPLC == "0": # Stops the loop when the input is 0
            break

        elif PlayPLC == "1": # Starts the questions if the input is 1
            while NumbSpg == 1: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 1:") # The next 3 prints is just to print information about question 1
                print("Hvad står PLC for? ")
                print("a: Programmerbar Logisk Controller \nb: Parkeret LadCykel \nc: Problematisk Langsom Computer \nd: Programmerbar Lækker Controller")
                if input(str("Indtast det rigtige svar: ")).lower() == "a": # Input the right answer
                    PointPLC += 1 # If the answer is right then add 1 point to PLC point
                    NumbSpg += 1 # Go to next question
                else:
                    PointPLC -= 1 # If the answer is wrong the minus 1 in PLC point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointPLC)
                print(NumbSpg)

            while NumbSpg == 2: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 2:") # The next 3 prints is just to print information about question 2
                print("Hvilken producent laver PLC'er af type ET200")
                print("a: Omron \nb: Beckhoff \nc: Wago \nd: Siemens")
                if input(str("Indtast det rigtige svar: ")).lower() == "d": # Input the right answer
                    PointPLC += 1 # If the answer is right then add 1 point to PLC point
                    NumbSpg += 1 # Go to next question
                else:
                    PointPLC -= 1 # If the answer is wrong the minus 1 in PLC point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointPLC)
                print(NumbSpg)
            
            while NumbSpg == 3: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 3:") # The next 3 prints is just to print information about question 3
                print("Hvor er + og - placeret når indgangene er opsat som sink")
                print("a: + ind på I1 og - ind på I0 \nb: + ind på I1 og - ind på COM \nc: + ind på COM og - ind på COM \nd: Der er ikke noget der hedder sink")
                if input(str("Indtast det rigtige svar: ")).lower() == "b": # Input the right answer
                    PointPLC += 1 # If the answer is right then add 1 point to PLC point
                    NumbSpg += 1 # Go to next question
                else:
                    PointPLC -= 1 # If the answer is wrong the minus 1 in PLC point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointPLC)
                print(NumbSpg)
                      
    return PointPLC