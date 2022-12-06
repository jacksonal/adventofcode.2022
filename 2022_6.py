# part 1 need to find index of first sequence of 4 characters that are unique from eachother
# part 2 need to find index of first sequence of 14 characters that are unique from eachother
from util import getFileContents
from timeit import default_timer as timer
def countCharsBeforeUniqueSequence(stream, length):
  for i in range(len(stream)):
    left = i
    right = i + length
    if len(set(datastream[left:right])) == length:
      return right

datastream = getFileContents('./input.txt').strip()

start = timer()
p1 = countCharsBeforeUniqueSequence(datastream,4)
end = timer()
print(p1, f'{(end-start) * 1000000} µs')
start = timer()
p2 = countCharsBeforeUniqueSequence(datastream,14)
end = timer()
print(p2, f'{(end-start) * 1000000} µs')