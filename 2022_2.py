from util import getLinesFromFile
from timeit import default_timer as timer
playScore = {
  'ROCK':1, 
  'PAPER':2, 
  'SCISSORS':3
}
winLookup = {
  'SCISSORS':'PAPER',
  'ROCK':'SCISSORS',
  'PAPER':'ROCK'
}

char2play = {
  'C':'SCISSORS', 
  'B':'PAPER', 
  'A':'ROCK',
  'Z':'SCISSORS',
  'X':'ROCK',
  'Y':'PAPER'
}

char2outcome={
  'X':'LOSE',
  'Y':'DRAW',
  'Z':'WIN'
}
outcomes={
  'ROCK':['SCISSORS', 'PAPER'],
  'PAPER':['ROCK', 'SCISSORS'],
  'SCISSORS':['PAPER', 'ROCK']
}
points={
  'WIN':6,
  'DRAW':3,
  'LOSE':0
}
def resultScore(me, them):
  if winLookup[me] == them : return 6
  elif me == them : return 3
  else: return 0

def scoreRoundP1(round):
  them, me = round.split()
  them = char2play[them]
  me = char2play[me]
  #print(f"They throw {char2play[them]}, I throw {char2play[me]}. {playScore[me]} for my throw and {resultScore(me,them)} for the result")
  return playScore[me] + resultScore(me,them)

def throw4outcome(opp, outcome):
  if outcome == 'DRAW': return opp
  elif outcome == 'WIN': return outcomes[opp][1]
  else: return outcomes[opp][0]

def scoreRoundP2(round):
  them, outcome = round.split()
  them = char2play[them]
  outcome = char2outcome[outcome]
  need2throw = throw4outcome(them,outcome)
  #print(f"They throw {them}, I Need to {outcome}. so i throw {need2throw} and score {playScore[need2throw]} for my throw and {points[outcome]} for the result")
  return playScore[need2throw] + points[outcome]

rounds = getLinesFromFile('.\\input.txt')
#print(rounds)
print('part 1:')
start = timer()
roundScores = [scoreRoundP1(x) for x in rounds]
#print(roundScores)
result1 = sum(roundScores)
end1 = timer()
print(result1)
print(f"{(end1 - start) * 1000000} µs")
print('part 2:')
start = timer()
roundScores = [scoreRoundP2(x) for x in rounds]
result1 = sum(roundScores)
end2 = timer()
print(sum(roundScores))
print(f"{(end2 - start) * 1000000} µs")