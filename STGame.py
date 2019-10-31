
def STGameSpg(): # Defenition for the ST game

    print("\nVelkommen til ST spillet som tager udgangspunkt i Tom Mejer Antonsens bog PLC styring med Structured Text(ST) \nDer vil være 3 opgaver, som giver 1 point for hvert rigtigt svar, og ved forkert svar vil der blive trukket 1 point fra.") # Welcome sentence

    PointST = 0 # Init of PointST

    PlayST = 0 # Init of PlayPLC

    NumbSpg = 1 # Init of NumbSpg

    while NumbSpg < 4: # While loop for the questions PLC game, only active when the numbspg is under 4. 
        #If the answer is right then add 1 point to the score, and if the answer is wrong then minus 1 point to the score

        PlayST = input(str("\nFor at komme igang med ST spillet tryk 1, for at gå videre til næste spil tryk 0: ")) # Input choice

        if PlayST == "0": # Stops the loop when the input is 0
            break

        elif PlayST == "1": # Starts the questions if the input is 1
                print("\nSpørgsmål 1:") # The next 3 prints is just to print information about answer 1
                print("Udfyld de tomme pladser i det følgende argument for en IF sætning med keywords fra ST: __ TempSensor = 5 ____") # The next 3 prints is just to print information about question 1
                print("                                                                                       TempLampe = 1_")
                print("                                                                                       _______")
                while NumbSpg == 1: # When NumbSpg is equal to 1 and then starts the answering
                    if input(str("Udfyld 1. frie plads: ")).upper() == "IF" and input(str("Udfyld 2. frie plads: ")).upper() == "THEN" and input(str("Udfyld 3. frie plads: ")) == ";" and input(str("Udfyld 4. frie plads: ")).upper() == "END_IF;": # Input to answering question 1
                        PointST += 1 # If the answer is right then add 1 point to ST point
                        NumbSpg += 1 # Go to next question
                    else:
                        PointST -= 1 # If the answer is wrong the minus 1 in ST point
                        print("Svaret er forkert prøv igen, kig i bogen PLC styring med Structured Text(ST) for mere information") # Print that the answer is wrong
                    print(PointST)
                    print(NumbSpg)

                print("\nSpørgsmål 2:") # The next 3 prints is just to print information about answer 2
                print("Udfyld de tomme pladser i det følgende argument for en FOR-løkke med keywords fra ST: ___ 1 __ 5 __") # The next 3 prints is just to print information about question 2
                print("                                                                                      Value := Value+1_")
                print("                                                                                      ________")
                while NumbSpg == 2: # When NumbSpg is equal to 1 and then starts the answering
                    if input(str("Udfyld 1. frie plads: ")).upper() == "FOR" and input(str("Udfyld 2. frie plads: ")).upper() == "TO" and input(str("Udfyld 3. frie plads: ")).upper() == "DO" and input(str("Udfyld 4. frie plads: ")).upper() == ";" and input(str("Udfyld 5. frie plads: ")).upper() == "END_FOR;": # Input to answering question 2
                        PointST += 1 # If the answer is right then add 1 point to ST point
                        NumbSpg += 1 # Go to next question
                    else:
                        PointST -= 1 # If the answer is wrong the minus 1 in ST point
                        print("Svaret er forkert prøv igen, kig i bogen PLC styring med Structured Text(ST) for mere information") # Print that the answer is wrong
                    print(PointST)
                    print(NumbSpg)
           
                print("\nSpørgsmål 3:") # The next 3 prints is just to print information about answer 3
                print("Udfyld de tomme pladser i det følgende argument for en CASE med keywords fra ST: ____ OpenValve __") # The next 3 prints is just to print information about question 3
                print("                                                                                 1 _ Open := 50_")
                print("                                                                                 2 _ Open := 100_")
                print("                                                                                 _________")
                while NumbSpg == 3: # When NumbSpg is equal to 1 and then starts the answering
                    if input(str("Udfyld 1. frie plads: ")).upper() == "CASE" and input(str("Udfyld 2. frie plads: ")).upper() == "OF" and input(str("Udfyld 3. frie plads: ")) == ":" and input(str("Udfyld 4. frie plads: ")) == ";" and input(str("Udfyld 5. frie plads: ")) == ":" and input(str("Udfyld 6. frie plads: ")) == ";" and input(str("Udfyld 7. frie plads: ")).upper() == "END_CASE;": # Input to answering question 3
                        PointST += 1 # If the answer is right then add 1 point to ST point
                        NumbSpg += 1 # Go to next question
                    else:
                        PointST -= 1 # If the answer is wrong the minus 1 in ST point
                        print("Svaret er forkert prøv igen, kig i bogen PLC styring med Structured Text(ST) for mere information") # Print that the answer is wrong
                print(PointST)
                print(NumbSpg)
                      
    return(PointST)

