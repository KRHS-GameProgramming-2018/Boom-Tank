import pygame, sys, math, random
from Block import *

def loadLevel(levelFile):
    f = open(levelFile, 'r')
    lines = f.readlines()
    f.close()
    
    level = []
    
    #Block Size is 50x50
    
    newLines = []
    for line in lines:
        newLine = ""
        for character in line:
            if not (character == '\n'):
                newLine += character
        newLines += [newLine]
    lines = newLines
    
    for line in lines:
        print line
        
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            if character == '#':
                level += [Block([x*50+25, y*50+25])]
             
    return level
    
    
    
# ~ loadLevel("Levels/1.lvl")
