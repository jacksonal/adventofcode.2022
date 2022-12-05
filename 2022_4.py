#need to clear space for supplies
#campsite divided into sections.
# elves grouped into pairs.
# each section has an ID. Each Elf assigned a range of IDs
# many of the elf pairs overlap in their ID range.
# some elves sections are fully contained within their partner's range

from util import getLinesFromFile
from timeit import default_timer as timer
def isContained(pair):
  r1 = pair[0]
  r2 = pair[1]
  if r1[0] >= r2[0] and r1[1] <= r2[1]:
    return 1
  else:
    return 0

def isOverlap(pair):
  r1 = pair[0]
  r2 = pair[1]
  if r1[0] >= r2[0] and r1[0] <= r2[1]:
    return 1
  elif r1[0] <= r2[1] and r1[1] >= r2[0]:
    return 1
  else:
    return 0

input = getLinesFromFile('./input.txt')
print('part 1')
start = timer()
#convert input to integer range pairs. also sort them so the smaller window is always first
pairs = [sorted([[int(id) for id in r.split('-')] for r in a.split(',')],key=lambda x: x[1]-x[0]) for a in input]
containedCount = sum([isContained(pair) for pair in pairs])
end = timer()
print(containedCount)
print(f'{(end-start)*1000000} µs')
overlapCount = sum([isOverlap(pair) for pair in pairs])
end = timer()
print(overlapCount)
print(f'{(end-start)*1000000} µs')