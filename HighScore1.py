
#import shelve

##import STGame 

#TotalScoreST = STGameSpg()
#TotalScoreRobot = RobotGame

#scoreFile = shelve.open('score.txt')

#def updateScore(newScore):
#  if('score' in scoreFile):
#    score = scoreFile['score']
#    if(newScore not in score):
#      score.insert(0, newScore)

#    score.sort()
#    ranking = score.index(newScore)
#    ranking = len(score)-ranking
#  else:
#    score = [newScore]
#    ranking = 1

#  print(score)
#  print(ranking)
#  scoreFile['score'] = score
#  print(TotalScore)
#  return ranking  

#newScore = int(input("New HighScore: \n"))
#updateScore(newScore)
