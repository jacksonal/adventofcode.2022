# need to get to a high point.
# input is a heightmap of the area.
#   grid of lowercase letters, a is lowest point z is highest
#   S is starting point, E is end point
# can only move at most to 1 elevation higher.
# can move to a square arbitrarily lower.
# can move cardinal directions only.
# count the fewest number of steps needed to get to E.

from util import getLinesFromFile
from string import ascii_lowercase
from collections import deque
import sys

heightTranslate= dict(zip(ascii_lowercase, range(26)))
heightTranslate['S'] = heightTranslate['a']
heightTranslate['E'] = heightTranslate['z']

class Hill:
  def __init__(self) -> None:
    self.canMoveTo = []
    self.height = None

def canMoveTo(origin, dest):
  return dest.height <= origin.height + 1

def searchPaths(origin, target, graph = None):
  """pass in the graph for part 2"""
  if graph is None:
    steps = {origin:0}
    queue = deque([origin])
  else:
    steps = dict()
    queue = deque()
    for row in graph:
      for node in row:
        if node.height == 0:
          steps[node] = 0
          queue.append(node)
  visited = set()
  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      if node == target:
        return steps[node]
      else:
        for n in node.canMoveTo:
          queue.append(n)
          if n not in steps:
            steps[n] = steps[node] + 1
  return -1

rows = getLinesFromFile('./input.txt')
hillGrid = []
lastrow = None
startHill = None
endHill = None
for r in rows:
  lastHill = None
  hillRow = []
  hillGrid.append(hillRow)
  for t in range(len(r)):
    hill = Hill()
    hillRow.append(hill)
    hill.height = heightTranslate[r[t]]
    if r[t] == 'S':
      startHill = hill
    if r[t] == 'E':
      endHill = hill
    if lastHill is not None:
      if canMoveTo(hill,lastHill):
        hill.canMoveTo.append(lastHill)
      if canMoveTo(lastHill,hill):
        lastHill.canMoveTo.append(hill)
      
    if lastrow is not None:
      if canMoveTo(hill,lastrow[t]):
        hill.canMoveTo.append(lastrow[t])
      if canMoveTo(lastrow[t], hill):
        lastrow[t].canMoveTo.append(hill)
    lastHill = hill
  lastrow = hillRow

# now find possible paths to end hill using breadth first search?
pathLength = searchPaths(startHill,endHill, hillGrid)
print(pathLength)