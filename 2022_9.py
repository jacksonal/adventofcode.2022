# rope physics
# rope has a head and a tail.
# head and tail occupy a space in a 2d grid.
# can occupy the same space
# it's a short rope. the head and tail should always be touching.
# every step, the head moves some distance in a cardinal direction.
# before the next step, the tail must catch up.
# will move diagonally until it is directly up/down/left/right. then move in cardinal direction until touching.
# how many spaces in the grid are visited by the tail??


from util import getLinesFromFile
from timeit import default_timer as timer

def isAdjacent(p1,p2):
  # unpack the coordinates
  x1, y1 = p1
  x2, y2 = p2

  # check if the coordinates are adjacent cardinally or diagonally, or overlapping
  return (x1 == x2 and y1 == y2) or (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 1)

def move(pos,direction):
  """return new position"""
  if direction == 'U':
    return (pos[0], pos[1] + 1)
  elif direction == 'D':
    return (pos[0], pos[1] - 1)
  elif direction == 'L':
    return (pos[0] - 1, pos[1])
  elif direction == 'R':
    return (pos[0] + 1, pos[1])
  
def moveCloser(startPos, targetPos):
  s1, s2 = startPos
  t1, t2 = targetPos

  if s1 == t1: # share an x axis
    if s2 < t2:
      return (s1, s2 + 1)
    else:
      return (s1, s2 - 1)
  elif s2 == t2: # share a y axis
    if s1 < t1:
      return (s1 + 1, s2)
    else:
      return (s1 - 1, s2)
  elif s1 < t1 and s2 < t2: #SW
    return (s1 + 1, s2 + 1)
  elif s1 > t1 and s2 < t2: #SE
    return (s1 - 1, s2 + 1)
  elif s1 < t1 and s2 > t2: #NW
    return (s1 + 1, s2 - 1)
  elif s1 > t1 and s2 > t2: #NE
    return (s1 - 1, s2 - 1)

instructions = getLinesFromFile('./input.txt')

begin = timer()
start = (0,0)
headPos = start
tailPos = start
visited = set()
visited.add(start)
# part 1
for instr in instructions:
  direction, distance = instr.split()
  for step in range(int(distance)):
    headPos = move(headPos, direction)
    while not isAdjacent(headPos,tailPos):
      tailPos = moveCloser(tailPos,headPos)
      visited.add(tailPos)
result = len(visited)
end = timer()
print('part 1:',result, f'{(end-begin) * 1000000} µs')

# part 2: now rope has 10 knots. each adjacent to the next. 
# same problem as before but with a longer rope. 
# knots move in same fashion by needing to be asjacent to next knot.

rope = [start] * 10
visited = set()
visited.add(start)
begin = timer()
for instr in instructions:
  direction, distance = instr.split()
  for step in range(int(distance)):
    rope[0] = move(rope[0], direction) # move head
    lead = rope[0]
    for knotindex in range(1,len(rope)): # update position of each knot
      while not isAdjacent(lead,rope[knotindex]):
        rope[knotindex] = moveCloser(rope[knotindex],lead)
      lead = rope[knotindex]
    visited.add(lead)

result = len(visited)
end = timer()
print('part 2:',result, f'{(end-begin) * 1000000} µs')