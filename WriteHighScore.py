import os

def NewUser(UserName, PointScore): # Definiton for writing a newuser to a .txt file

    #UserName = str(input("Write user name: ")) New username input 

    UserFile = open("UserFile.txt", 'a+' ) # Open file for reading and appending 
    UserFile.writelines([UserName,", ",PointScore,"\n"]) # Write username and topscore to file with , as seperation and a \n to write username and topscore vertical in file  
    #User.write("\n")
       
    UserFile.close() # Close file when the writing is done

    os.startfile("UserFile.txt")
