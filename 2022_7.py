#running device. needs to execute a series of shell commands to see what's in the file system
# filesystem consists of files and directories
# root dir is /
# input is the shell commands (begin with $) and output
# commands are:
#   cd x (move into directory x)
#   cd .. (move out one level)
#   cd / (move to the root dir)
#   ls (list the contents of current dir)
#     output: 123 abc means abc is a file of size 123 in this directory
#     output: dir xyz means xyz is a subdirectory
# problem: need to determine the size of directories in the system
# part 1 find all dirs with a size of at most 100000 and sum these.
# example: dir a contains dir b. dir b is size 100, dir a is size 300 (200 files + 100 in the sub dir). answer is 300 + 100 = 400

from util import getLinesFromFile
from timeit import default_timer as timer

class Directory:
  def __init__(self) -> None:
    self.subDirectories = []
    self.fileContents = set()
    self.name = ''
    self.parentDir = None
  
  def getDir(self, dirName):
    """return a dir object with dirName and this as its parent"""
    found = next((d for d in self.subDirectories if d.name == dirName), None)
    if found is None:
      #create dir
      found = Directory()
      found.name = dirName
      found.parentDir = self
      self.subDirectories.append(found)
    return found
  def registerFile(self,fileName,fileSize):
    self.fileContents.add((fileName,fileSize))
  
  def calculateSize(self):
    self.size = sum([d.calculateSize() for d in self.subDirectories]) + sum([f[1] for f in self.fileContents])
    return self.size

  def getAllSubDirs(self):
    ret = [(sd.name,sd.size) for sd in self.subDirectories]
    [ret.extend(d.getAllSubDirs()) for d in self.subDirectories]
    return ret

console = getLinesFromFile('./input.txt')
root = Directory()
curdir = root

#build directory tree structure
for line in console:
  tokens = line.split()
  if tokens[0] == '$': #user command
    if tokens[1] == 'cd':
      if tokens[2] == '/':
        curdir = root
      elif tokens[2] == '..':
        curdir = curdir.parentDir
      else:
        curdir = curdir.getDir(tokens[2])
    elif tokens[1] == 'ls':
      pass
  else: # file or directory listing
    if tokens[0] == 'dir':
      curdir.getDir(tokens[1]) #shortcut to create the directory
    else:
      curdir.registerFile(tokens[1],int(tokens[0]))
      
start1 = timer()
spaceUsed = root.calculateSize()

dirList = sorted(root.getAllSubDirs(),key=lambda sd: sd[1])
p1result = sum([d[1] for d in dirList if d[1] <= 100000])
end1 = timer()

start2 = timer()
spaceAvailable = 70000000 - spaceUsed
#need to find a dir that when deleted will result in at least 30000000
targetDirSize = 30000000 - spaceAvailable
p2result = next((d[1] for d in dirList if d[1] >= targetDirSize))
end2 = timer()

print(p1result, f'{(end1-start1) * 1000000} µs')
print(p2result, f'{(end2-start2) * 1000000} µs')