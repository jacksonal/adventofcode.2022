# instruction stream.
# 1 instruction per cycle
# cycles start at 1
# addx V adds the V value to register x. takes 2 cycles to complete.
# Do not move to next instruction until previous one completes.
# sum the register values at cycle 20, 60, 100, ..., 220

from util import getLinesFromFile

instructions = [int(line.split()[1]) if line.startswith('a') else 0 for line in getLinesFromFile('./input.txt')]
#instructions = [0,3,-5]
reg = 1
instrPointer = 0
toadd = None
sigStrengths = []
spriteMask = (0,2)
screenarray = []
for cycle in range(1,241):
  crtPointer = (cycle - 1) % 40
  beginAdd = False
  #begin cycle
  if instructions[instrPointer] == 0:
    #print(cycle, spriteMask, f'instr {instrPointer}','noop', f'reg: {reg}')
    instrPointer += 1
  elif toadd is None:
    toadd = instructions[instrPointer]
    #print(cycle, spriteMask, f'instr {instrPointer}', f'begin add {toadd}', f'reg: {reg}')
    beginAdd = True # add instr takes 2 cycles to complete.

  #mid cycle
  if (cycle) % 40 == 20:
    #print(cycle,reg, cycle * reg)
    sigStrengths.append(cycle * reg)
  # draw pixel
  if crtPointer >= spriteMask[0] and crtPointer <= spriteMask[1]:
    screenarray.append('#')
  else:
    screenarray.append('.')
  
  #end cycle
  if not beginAdd and toadd is not None:
    reg += toadd
    spriteMask = (reg-1,reg+1)
    #print(cycle, spriteMask, f'instr {instrPointer}', f'finish add {toadd}', f'reg: {reg}')
    toadd = None
    instrPointer += 1

print('PART 1:', sum(sigStrengths))

#part 2
# x register controls horizontal position of a sprite
# sprite is 3 px wide
# x reg sets position of the middle of the sprite
# crt is 40 wide and 6 high (0 index)
# pixels drawn left to right, top to bottom
# crt draws 1 pixel per cycle then moves to next pixel. i.e. cycle 1 draw the 1st pixel in the 1st row. cycle 40, draw the last pixel in the first row
# if any part of the 3 px wide sprite covers the pixel being drawn, the pixel is drawn lit, otherwise it's drawn dark.
print('part 2:')
for rowstart in range(0,240,40):
  print(''.join(screenarray[rowstart:rowstart+40]))

