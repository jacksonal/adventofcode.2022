# monkeys have stolen items from my pack
# monkeys have following attributes
#   starting items - my worry level for each item in the order they will be inspected.
#   Operation - how my worry level changes as the monkey inspects items
#   Test - how the monkey determines what to do based on my worry level
# after a monkey inspects an item, before it tests my worry, I am relieved it isn't damaged and my worry level is divided by 3 rounded down
# monkeys take turns inspecting and throwing items
# on a turn it inspects and throws all items it is holding one at a time, in order
# monkey 0 goes first, etc. until the ROUND completes
# an item thrown to a monkey puts it at the end of their list.

# part 1: count the total number of items each monkey inspects over 20 rounds
# calculate the monkey business score by multiplying the # of items inspected by the two most active monkeys
from util import getFileContents

class Monkey:
  def __init__(self, 
                worryLevels, 
                worryFunc, 
                testDivisor, 
                targets) -> None:
    self.items = worryLevels
    self.updateWorry = worryFunc
    self.worryDivisibleTest = testDivisor
    self.targetMonkeys = targets
    self.inspectCount = 0

def buildMonkeyMap() -> dict:
  map = dict()
  for m in getFileContents('./input.txt').split('\n\n'):
    print(m)
    lines = m.split('\n')
    label = int(lines[0][-2])
    items = [int(i) for i in lines[1].split(':')[1].split(',')]
    worryop = eval('lambda old:' + lines[2].split('=')[1])
    divBy = int(lines[3].split()[-1])
    targets = (int(lines[4][-1]), int(lines[5][-1]))
    
    map[label] = Monkey(items,worryop, divBy, targets)
  return map

monkeyMap = buildMonkeyMap()
for round in range(10000):
  #print(f'ROUND {round}')
  for id in range(len(monkeyMap)):
    monkey = monkeyMap[id]
    # inspect, update worry, throw each item
    #print(f'monkey {id}')
    while(len(monkey.items) > 0):
      current = monkey.items.pop(0)
      #print(f'\tinspecting item {current}')
      current = monkey.updateWorry(current)
      #print(f'\t\tupdating item to {current}')
      #monkey gets bored, decrease worry level only in part 1
      #current = current // 3
      #print(f'decrease worry to {current}')
      monkey.inspectCount += 1
      current = current % 9699690 #must mod the value by LCM of all the divisors. why? to make sure it doesn't affect the divisibility by the other test values.
      if current % monkey.worryDivisibleTest == 0:
        #print(f'\t\t{current} is divisible by {monkey.worryDivisibleTest}. pass to {monkey.targetMonkeys[0]}')
        monkeyMap[monkey.targetMonkeys[0]].items.append(current)
      else:
        #print(f'\t\t{current} is not divisible by {monkey.worryDivisibleTest}. pass to {monkey.targetMonkeys[1]}')
        monkeyMap[monkey.targetMonkeys[1]].items.append(current)

inspectScores = sorted([m.inspectCount for m in monkeyMap.values()])
print(inspectScores)
print(inspectScores[-1] * inspectScores[-2])

# part 2:
# no longer divide worry levels by 3.
# calculate monkey business score after 10,000 rounds
# how to track extremely large worry scores?