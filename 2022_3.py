#rucksacks have 2 large compartments
#each sack has items.
#all items of a given type need to be in the same compartment.
#a rucksack has the same number of items in each compartment

from util import getLinesFromFile
from string import ascii_lowercase, ascii_uppercase
from timeit import default_timer as timer

priorityTable = dict(zip(ascii_lowercase + ascii_uppercase, range(1,53)))

def getCompartments(container):
    compartmentSize = int(len(container)/2)
    return (set(container[:compartmentSize]),set(container[compartmentSize:]))

def groupsOf(iter,size):
    for i in range(0,len(iter),size):
        yield iter[i:i+size]

def findBadge(group):
    return group.pop().intersection(group.pop()).intersection(group.pop()).pop()
packList = getLinesFromFile('./input.txt')

print('part 1')
start = timer()
sacks = [getCompartments(sack) for sack in packList]
overlaps = [a.intersection(b).pop() for a,b in sacks]
prioritySum = sum([priorityTable[item] for item in overlaps])
end = timer()
print(prioritySum)
print(f'solved in {(end-start)*1000000} μs')

start = timer()
groups = groupsOf([set(pack)for pack in packList],3)
groupBadges = [findBadge(g) for g in groups]
prioritySum = sum([priorityTable[badge] for badge in groupBadges])
end = timer()
print(prioritySum)
print(f'solved in {(end-start)*1000000} μs')