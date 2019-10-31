
def PythonGameSpg(): # Defenition for the Python game

    print("\nVelkommen til Python spillet \nDer vil være 3 opgaver, som giver 1 point for hvert rigtigt svar, og ved forkert svar vil der blive trukket 1 point fra.") # Welcome sentence

    PointPython = 0 # Init of PointPLC

    PlayPython = 0 # Init of PointPLC

    NumbSpg = 1 # Init of PointPLC

    while NumbSpg < 4: # While loop for the questions PLC game, only active when the numbspg is under 4. 
        #If the answer is right then add 1 point to the score, and if the answer is wrong then minus 1 point to the score

        PlayPython = input(str("\nFor at komme igang med Python spillet tryk 1, for at stoppe tryk 0: ")) # Input choice

        if PlayPython == "0": # Stops the loop when the input is 0
            break

        elif PlayPython == "1": # Starts the questions if the input is 1
            while NumbSpg == 1: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 1:") # The next 3 prints is just to print information about question 1
                print("Hvad/hvem er sproget Python opkaldt efter?")
                print("a: En lang tyk slange \nb: Monty Python \nc: En fisk \nd: Et cykel mærke")
                if input(str("Indtast det rigtige svar: ")).lower() == "b": # Input the right answer
                    PointPython += 1 # If the answer is right then add 1 point to python point
                    NumbSpg += 1 # Go to next question
                else:
                    PointPython -= 1 # If the answer is wrong the minus 1 in python point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointPython)
                print(NumbSpg)

            while NumbSpg == 2: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 2:") # The next 3 prints is just to print information about question 2
                print("Hvem opfandt Python?")
                print("a: Donald Trump \nb: Snakeman \nc: Tom Mejer Antonsen \nd: Guido van Rossum")
                if input(str("Indtast det rigtige svar: ")).lower() == "d": # Input the right answer
                    PointPython += 1 # If the answer is right then add 1 point to python point
                    NumbSpg += 1 # Go to next question
                else:
                    PointPython -= 1 # If the answer is wrong the minus 1 in python point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointPython)
                print(NumbSpg)
            
            if NumbSpg == 3: # When NumbSpg is equal to 1 and then starts the questions
                print("\nSpørgsmål 3:") # The next 3 prints is just to print information about question 3
                print("Hvad bruges print() til?")
                print("a: Til at printe til console \nb: Til at printe på skolens printer \nc: Til at printe koden i PDF \nd: Det er ikke en funktion i Python")
                if input(str("Indtast det rigtige svar: ")).lower() == "a": # Input the right answer
                    PointPython += 1 # If the answer is right then add 1 point to python point
                    NumbSpg += 1 # Go to next question
                else:
                    PointPython -= 1 # If the answer is wrong the minus 1 in python point
                    print("Svaret er forkert, prøv igen") # Print that the answer is wrong
                    #NumbSpg += 1
                print(PointPython)
                print(NumbSpg)
                      
    return PointPython