
import pygame, sys, math, random
from Block import *
from Bullet import *

def loadLevel(levelFile):
    f = open(levelFile, 'r')
    lines = f.readlines()
    f.close()
    
    level = level = {"Block":[],
             "playerTank":[0,0],
             "enemyTank":[],
             }
    
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
                level["Block"] += [([x*50+25, y*50+25])]
            if character == 'x':
                level["enemyTank"] += [(4, [x*50+25, y*50+25])]
            if character == 'y':
                level["playerTank"] += [(4, [x*50+25, y*50+25])]             
    return level
    
    
    
# ~ loadLevel("Levels/1.lv)
