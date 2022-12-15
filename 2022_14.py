# sand falling from a cave ceiling.
# 1 grain at a time. next grain won't fall until the previous has come to a rest.
# grain will fall to the spot below it if it can.
# tile below blocked? will move down to the left.
#   down/left blocked? move down/right. else rest and this tile is now blocked.
# how many grains of sand need to fall before all new sand falls into the void?

from util import getLinesFromFile
import sys

def isVertical(p1,p2):
  return p1[0] == p2[0] and p1[1] != p2[1]

def isHorizontal(p1,p2):
  return p1[1] == p2[1] and p1[0] != p2[0]

def getIncrementer(x1,x2):
  if x1 < x2:
    return range(0,x2 - x1 + 1)
  else:
    return range(x2 - x1, 1)

def printTiles(xBounds,yBounds,blockers):
  for y in range(yBounds[0],yBounds[1] + 1):
    row = []
    for x in range(xBounds[0],xBounds[1] + 1):
      #print(x,y)
      if (x,y) in blockers:
        row.append('#')
      else:
        row.append('.')
    print(''.join(row))

def canOccupy(tile, blockedTiles):
  return tile not in blockedTiles

lines = getLinesFromFile('./input.txt')

blocked = set()
lowestY = 0
lowestX = sys.maxsize
highestX = 0
for path in lines: #track blocked tiles
  #print(path)
  prevPoint = None
  for point in [tuple(int(coord) for coord in p.split(',')) for p in path.split('->')]:
    if point[1] > lowestY:
      #print('lower point found', point)
      lowestY = point[1]
      caveFloor = lowestY + 2
    if point[0] < lowestX:
      lowestX = point[0]
    if point[0] > highestX:
      highestX = point[0]

    print(prevPoint, '->', point)
    if prevPoint is not None:
      if isVertical(prevPoint,point):
        #print('vertical segment')
        increments = getIncrementer(prevPoint[1],point[1])
        for tile in [(point[0],prevPoint[1] + i) for i in increments]:
          #print('blocking', tile)
          blocked.add(tile)
      elif isHorizontal(prevPoint,point):
        #print('horizontal segment')
        increments = getIncrementer(prevPoint[0],point[0])
        for tile in [(prevPoint[0] + i,point[1]) for i in increments]:
          #print('blocking', tile)
          blocked.add(tile)
    prevPoint = point

#printTiles((lowestX,highestX),(0,lowestY),blocked)

# start droppin sand
origin = (500,0)
sandLoc = origin
grainCount = 0
while True:
  #if sandLoc[1] > lowestY:
   # break #into the void
  
  if sandLoc[1] + 1 == caveFloor:
    #come to rest
    blocked.add(sandLoc)
    grainCount += 1
    sandLoc = origin
    continue

  if canOccupy((sandLoc[0], sandLoc[1] + 1),blocked): #check below
    sandLoc = (sandLoc[0], sandLoc[1] + 1)
  elif canOccupy((sandLoc[0] - 1, sandLoc[1] + 1), blocked): #check diagonal left
    sandLoc = (sandLoc[0] - 1, sandLoc[1] + 1)
  elif canOccupy((sandLoc[0] + 1, sandLoc[1] + 1), blocked): #check diagonal right
    sandLoc = (sandLoc[0] + 1, sandLoc[1] + 1)
  else:
    # we rest
    blocked.add(sandLoc)
    grainCount += 1
    if sandLoc == origin:
      break #no more sand can be dropped
    sandLoc = origin
#print(sorted(blocked,key=lambda x: x[1]))

#display the tiles
#print(lowestX,highestX)
#print('FINAL')
#printTiles((lowestX,highestX),(0,lowestY),blocked)

print(grainCount)