import pygame, sys, math, random
import pygame, sys, math, random         
from Turret import *
from PlayerTurret import *
from PlayerTankBody import *
from Levels import *
from EnemyTank import *
from PlayerTurret2 import *
from Bullet import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

playerTurret = PlayerTurret(5, [width/2, height/2])
enemyTurret = PlayerTurret2(8, [width/5, height/5])
playerTank = PlayerTankBody(2, [width/3, height/3])
enemyTank = PlayerEnemy(6, [width/4, height/4])


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

playerTank.rect.center = [85,85]
enemyTank.rect.center = [500,500]

balls = []
bullets = []


mposX = 0
mposY = 0

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        #if bullet.collide(playerTank):
        if event.type == pygame.MOUSEMOTION:
            playerTurret.rotate(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerTank.go("up")
            if event.key == pygame.K_a:
                playerTank.go("left")
            if event.key == pygame.K_s:
                playerTank.go("down")
            if event.key == pygame.K_d:
                playerTank.go("right")
            if event.key == pygame.K_SPACE:
                print "shooting"
                bullets += [playerTurret.shoot()]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerTank.go("sup")
            if event.key == pygame.K_a:
                playerTank.go("sleft")
            if event.key == pygame.K_s:
                playerTank.go("sdown")
            if event.key == pygame.K_d:
                playerTank.go("sright")
        
        
        
    for bullet in bullets: 
        bullet.update(size)
        bullet.collide(enemyTank)
        if bullet.collide(enemyTank):
            PlayerEnemy.explode(enemyTank, bullet)
        for block in blocks:
            bullet.collide(block)
        bullet.bounceWall(size)
        if not bullet.living:
            bullets.remove(bullet)
        
    print len(bullets)
        
    playerTank.collide(enemyTank)
    
   
    for block in blocks:
        playerTank.collide(block)
        
        

    
                
    enemyTank.update(size)  
    enemyTurret.update(size, enemyTank.rect.center)
    playerTank.update(size)
    playerTurret.update(size, playerTank.rect.center)
    
    
    screen.fill(bgColor)
    screen.blit(bgPic, bgPicrect)
    screen.blit(enemyTank.image, enemyTank.rect)
    screen.blit(enemyTurret.image, enemyTurret.rect)
    screen.blit(playerTank.image, playerTank.rect)
    screen.blit(playerTurret.image, playerTurret.rect)
    for block in blocks:
        screen.blit(block.image, block.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    
            
    pygame.display.flip()
    clock.tick(40)
    #print clock.get_fps()
