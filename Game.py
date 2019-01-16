import pygame, sys, math, random
import pygame, sys, math, random
from Turret import *
from PlayerTurret import *
from TankBody import *
from PlayerTankBody import *
from Levels import *
#from Bullet import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

player1 = PlayerTurret(5, [width/2, height/2])
player2 = PlayerTankBody(2, [width/3, height/3])

bgColor = 0,0,0

bgPic = pygame.image.load("wood.png")
bgPicrect = bgPic.get_rect()

lev=1
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=2
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=3
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=4
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=5
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=6
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=7
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=8
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=9
blocks=loadLevel("Levels/"+str(lev)+".lvl")

lev=10
blocks=loadLevel("Levels/"+str(lev)+".lvl")

balls = []

mposX = 0
mposY = 0

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            player1.rotate(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player2.go("up")
            if event.key == pygame.K_a:
                player2.go("left")
            if event.key == pygame.K_s:
                player2.go("down")
            if event.key == pygame.K_d:
                player2.go("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2.go("sup")
            if event.key == pygame.K_a:
                player2.go("sleft")
            if event.key == pygame.K_s:
                player2.go("sdown")
            if event.key == pygame.K_d:
                player2.go("sright")
       # if event.type == pygame.MOUSECLICK:
           # if event.key == pygame.K_
        
    
                
                
    player2.update(size)
    player1.update(size, player2.rect.center)
    screen.fill(bgColor)
    screen.blit(bgPic, bgPicrect)
    screen.blit(player2.image, player2.rect)
    screen.blit(player1.image, player1.rect)
    for block in blocks:
        screen.blit(block.image, block.rect)
            
    pygame.display.flip()
    clock.tick(40)
    print clock.get_fps()
