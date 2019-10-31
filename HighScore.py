

def HighScoreFile(): # Definition to read and print the score from .txt file
    UserRead = open("UserFile.txt", 'r+') # Open file for reading and writing 
    store1 = UserRead.read().splitlines() # Reads the lines and splits them so there is no \n when the variable is printet
    print(store1) # print the scores from file

## lånt fra http://programarcadegames.com/python_examples/show_file.php?file=high_score.py

#def get_high_score():
#    # default high score
#    high_score = 0
 
#    # try to read the high score from a file
#    try:
#        high_score_file = open("highscore.txt", "r")
#        high_score = int(high_score_file.read())
#        high_score_file.close()
#        print("the high score is", high_score)
#    except ioerror:
#        # error reading file, no high score
#        print("there is no high score yet.")
#    except valueerror:
#        # there's a file there, but we don't understand the number.
#        print("i'm confused. starting with no high score.")
 
#    return high_score
 
 
#def save_high_score(new_high_score):
#    try:
#        # write the file to disk
#        high_score_file = open("highscore.txt", "a+")
#        high_score_file.write(str(new_high_score))
#        high_score_file.write("\n")
#        high_score_file.close()
#    except ioerror:
#        # hm, can't write it.
#        print("unable to save the high score.")
 
 
#def main():
#    # main program is here.
#    # get the high score
#    high_score = get_high_score()
 
#    # get the score from the current game
#    current_score = 0
#    try:
#        # ask the user for his/her score
#        current_score = int(input("what is your score? "))
#    except valueerror:
#        # error, can't turn what they typed into a number
#        print("i don't understand what you typed.")
 
#    # see if we have a new high score
#    if current_score > high_score:
#        # we do! save to disk
#        print("yea! new high score!")
#        save_high_score(current_score)
#    else:
#        print("better luck next time.")
 
## call the main function, start up the game
#if __name__ == "__main__":
#    main()

