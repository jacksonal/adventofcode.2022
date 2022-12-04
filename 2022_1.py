from util import getLinesFromFile
from timeit import default_timer as timer

def accumulateCalories(input):
  packs = []
  pack = 0
  for snack in input:
    if len(snack) == 0 or snack.isspace():
      packs.append(pack)
      pack = 0
    else:
      pack += int(snack)
  return packs

start = timer()
lines = getLinesFromFile('./input.txt')
calsInPacks = accumulateCalories(lines)
calsInPacks.sort(reverse=True)
p1 = calsInPacks[0]

end1 = timer()
p2 = sum(calsInPacks[:3])
end2 = timer()
print(p1)
print(f"{(end1 - start) * 1000000} µs")
print(p2)
print(f"{(end2 - start) * 1000000} µs")