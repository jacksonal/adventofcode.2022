# need to rearrange stacks of crates.
# have starting config and instruction set for how they will be moved
# what are the crate labels at the top of each stack at the end?
# Sample Input:
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

from util import getLinesFromFile
from timeit import default_timer as timer

def runInstructionP1(instr, stackMap):
  args = instr.split()[1::2]
  numCrates = int(args[0])
  originStack = args[1]
  targetStack = args[2]

  for cnt in range(numCrates):
    stackMap[targetStack].append(stackMap[originStack].pop())

def runInstructionP2(instr, stackMap):
  args = instr.split()[1::2]
  numCrates = int(args[0])
  originStack = args[1]
  targetStack = args[2]
  
  stackMap[targetStack].extend(stackMap[originStack][-numCrates:])
  stackMap[originStack] = stackMap[originStack][:-numCrates]

def initStacks(rawStacks):
  rawStackIds = rawStacks[-1].split()
  stacks = {}
  for sid in rawStackIds:
    stacks[sid] = []

  for row in rawStacks[-2::-1]:
    for crate in zip(rawStackIds,row[1::4]):
      if not crate[1].isspace():
        stacks[crate[0]].append(crate[1])
  return stacks

lines = getLinesFromFile('./input.txt')

rawStacks = []
rawInstructions = []
currList = rawStacks
for l in lines:
  if l == '':
    currList = rawInstructions
  else:
    currList.append(l)

#part 1: pop items one at a time
# create stack structures
stacks = initStacks(rawStacks)
start = timer()
#Now we have our stacks as lists with the top item in the last position
for instr in rawInstructions:
  runInstructionP1(instr, stacks)
end = timer()
print(''.join([stacks[id][-1] for id in sorted(stacks.keys())]))
print(f'{(end-start) * 1000000}  µs')
#reset for part 2: maintain order of popped items on next stack.
# create stack structures
stacks = initStacks(rawStacks)
#Now we have our stacks as lists with the top item in the last position
start = timer()
for instr in rawInstructions:
  runInstructionP2(instr, stacks)
end= timer()
print(''.join([stacks[id][-1] for id in sorted(stacks.keys())]))
print(f'{(end-start) * 1000000}  µs')