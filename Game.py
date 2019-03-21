import pygame, sys, math, random
import pygame, sys, math, random         
from Turret import *
from PlayerTurret import *
from PlayerTankBody import *
from Levels import *
from EnemyTank import *
from Bullet import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

playerTurret = PlayerTurret(5, [width/2, height/2])
playerTank = PlayerTankBody(3, [width/3, height/3])
enemyTanks = []


bgColor = 0,0,0

bgPic = pygame.image.load("wood.png")
bgPicrect = bgPic.get_rect()

lev=1
blocks, playerTank.rect.center, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
for c in enemyTankCenters:
    enemyTanks += [PlayerEnemy(3, c)]

balls = []
bullets = []


mposX = 0
mposY = 0


#mode = "start"

#go = True


# while go:
    # startimage = pygame.transform.scale(pygame.image.load("wood.png"), [width,height])
    # #deathimage = pygame.transform.scale(pygame.image.load("wood.png"), [width,height])
   # #STARTSCREEN
 
    # while mode == "start":
        # for event in pygame.event.get():
            # #print event.type
            # if event.type == pygame.QUIT:
                # sys.exit()
            # if event.type == pygame.KEYDOWN:
                # #pygame.time.delay(1000)
                # mode = "play"
        # screen.blit(startimage, (0,0))
        # pygame.display.flip()
        # clock.tick(60)

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            playerTurret.rotate(event.pos)
        if event.type == pygame.KEYDOWN:
            if playerTank:
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
            if playerTank:
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
        for enemyTank in enemyTanks:
            bullet.collide(enemyTank)
        for block in blocks:
            bullet.collide(block)
            
        bullet.bounceWall(size)
        if not bullet.living:
            bullets.remove(bullet)
        for enemyTank in enemyTanks:
            enemyTank.explode(bullet)
    if playerTank:
        for Block in blocks:
            playerTank.collide(Block)  
            for enemyTank in enemyTanks:  
                enemyTank.collide(Block)    
        
    enemyTank.collide(Block)
      
        
    print len(bullets)
    
    for enemyTank in enemyTanks:
        if playerTank:
            if playerTank.collide(enemyTank):
                playerTank = None
    for enemyTank in enemyTanks:
        enemyTank.turret.update(size, enemyTank.rect.center)
    if playerTank:
        playerTank.update(size)
        playerTurret.update(size, playerTank.rect.center)
    if playerTank:
        for enemyTank in enemyTanks:
            enemyTank.update(size, playerTank.rect.center)
    for enemyTank in enemyTanks:
        if not enemyTank.living:
            enemyTanks.remove(enemyTank)
        if len(enemyTanks) <= 0:
            if lev < 10:
                lev += 1
            else:
                lev = 1
            blocks, playerTank.rect.center, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
            for c in enemyTankCenters:
                enemyTanks += [PlayerEnemy(3, c)]
                
                
    
    screen.fill(bgColor)
    screen.blit(bgPic, bgPicrect)
    for enemyTank in enemyTanks:
        screen.blit(enemyTank.image, enemyTank.rect)
        screen.blit(enemyTank.turret.image, enemyTank.turret.rect)
    if playerTank:
        screen.blit(playerTank.image, playerTank.rect)
        screen.blit(playerTurret.image, playerTurret.rect)
    for block in blocks:
        screen.blit(block.image, block.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    
            
    pygame.display.flip()
    clock.tick(40)
    print clock.get_fps()
