import sys

def getLinesFromFile(path):
  with open(path) as f:
    lines = f.readlines()
    return [l.rstrip('\n') for l in lines]

def getFileContents(path):
  with open(path) as f:
    content = f.read()
    return content