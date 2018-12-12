#test caden
import pygame, sys, math, random
from tank import *
from playertank import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

player1 = PlayerBall(5, [width/2, height/2])

bgColor = 0,255,0

mposX = 0
mposY = 0

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            player1.rotate(event.pos)
            
   
    screen.fill(bgColor)
    screen.blit(player1.image, player1.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()
