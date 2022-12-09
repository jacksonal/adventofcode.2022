# a cartesian grid of trees
# each tree is a certain height (int)
# viewed from the north/south/east/west a tree is visible if all trees between it and the outter edge of the grid are smaller
# how many trees are seen??

from util import getLinesFromFile
from timeit import default_timer as timer

class Tree:
  def __init__(self) -> None:
    self.height = 0
    self.up = None
    self.down = None
    self.left = None
    self.right = None
    self.scenicScore = 0
  
  def isSeenFrom(self, direction, neighbor, height):
    #print(f'looking {direction}')

    if neighbor is None:
      #print('edge')
      return True
    
    if direction == 'u':
      next = neighbor.up
    elif direction == 'd':
      next = neighbor.down
    elif direction == 'l':
      next = neighbor.left
    elif direction == 'r':
      next = neighbor.right

    if neighbor.height < height:
      #print(f'I am {height} so I can see past {neighbor.height}')
      return neighbor.isSeenFrom(direction,next,height)
    else:
      #print(f'I am {height} so I can NOT see past {neighbor.height}')
      return False

  def isSeenFromEdge(self):
    if not self.up or not self.down or not self.left or not self.right: # I am the edge
      return True
    return self.isSeenFrom('u', self.up, self.height) or self.isSeenFrom('d',self.down, self.height) or self.isSeenFrom('l',self.left,self.height) or self.isSeenFrom('r',self.right, self.height)

  def treesSeen(self, direction, fromHeight):
    if direction == 'u':
      next = self.up
    elif direction == 'd':
      next = self.down
    elif direction == 'l':
      next = self.left
    elif direction == 'r':
      next = self.right

    if next is None:
      return 0
    elif fromHeight > next.height:
      return 1 + next.treesSeen(direction,fromHeight)
    else:
      return 1

  def computeScenicScore(self):
    """multiply how many trees can be seen from this tree in each direction"""
    self.scenicScore = self.treesSeen('u',self.height) * self.treesSeen('d',self.height) * self.treesSeen('l',self.height) * self.treesSeen('r',self.height)
    return self.scenicScore

rows = getLinesFromFile('./input.txt')

#build the tree graph
treeGrid = []
lastrow = None
for r in rows:
  heights = [int(t) for t in r]
  lastTree = None
  treeRow = []
  treeGrid.append(treeRow)
  for t in range(len(heights)):
    tree = Tree()
    treeRow.append(tree)
    tree.height = heights[t]
    tree.left = lastTree
    if lastTree is not None:
      lastTree.right = tree
    if lastrow is not None:
      tree.up = lastrow[t]
      lastrow[t].down = tree
    lastTree = tree
  lastrow = treeRow

start = timer()
seenCount = sum([len([t for t in row if t.isSeenFromEdge()]) for row in treeGrid])
end = timer()
print(seenCount, f'{(end-start) * 1000000} µs')
start = timer()
bestScore = max([max([t.computeScenicScore() for t in row]) for row in treeGrid])
end = timer()
print(bestScore, f'{(end-start) * 1000000} µs')
