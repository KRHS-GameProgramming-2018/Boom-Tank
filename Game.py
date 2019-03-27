import pygame, sys, math, random
import pygame, sys, math, random         
from Turret import *
from PlayerTurret import *
from PlayerTankBody import *
from Levels import *
from EnemyTank import *
from Bullet import *
from TankBody import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

blocks = pygame.sprite.Group()
playerTanks = pygame.sprite.Group()
enemyTanks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()

Block.containers = (blocks, all)
PlayerTurret.containers = (playerTanks, all)
PlayerTankBody.containers = (playerTanks, all)
EnemyTank.containers = (enemyTanks, all)
Bullet.containers = (bullets, all)

player1 = PlayerTankBody(3, [width/3, height/3])


bgColor = 0,0,0

bgPic = pygame.image.load("wood.png")
bgPicrect = bgPic.get_rect()

lev=1
player1.rect.center, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
for c in enemyTankCenters:
    EnemyTank(3, c)

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
            player1.turret.rotate(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.go("up")
            if event.key == pygame.K_a:
                player1.go("left")
            if event.key == pygame.K_s:
                player1.go("down")
            if event.key == pygame.K_d:
                player1.go("right")
            if event.key == pygame.K_SPACE:
                print "shooting"
                player1.turret.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: 
                player1.go("sup")
            if event.key == pygame.K_a:
                player1.go("sleft")
            if event.key == pygame.K_s:
                player1.go("sdown")
            if event.key == pygame.K_d:
                player1.go("sright")
       
            
        
        
        
    # for bullet in bullets: 
        # bullet.update(size)
        # for enemyTank in enemyTanks:
            # bullet.collide(enemyTank)
        # for block in blocks:
            # bullet.collide(block)
            
        # bullet.bounceWall(size)
        # if not bullet.living:
            # bullets.remove(bullet)
        # for enemyTank in enemyTanks:
            # enemyTank.explode(bullet)
    # if player1:
        # for Block in blocks:
            # player1.collide(Block)  
            # for enemyTank in enemyTanks:  
                # enemyTank.collide(Block)    
        
    #enemyTank.collide(Block)
      
        
    
    
    # for enemyTank in enemyTanks:
        # if player1:
            # if player1.collide(enemyTank):
                # playerTank = None
                
    # print len(bullets)
    
    # for enemyTank in enemyTanks:
        # enemyTank.turret.update(size, enemyTank.rect.center)
    # if player1:
        # player1.update(size)
        # playerTurret.update(size, player1.rect.center)
    # if player1:
        # for enemyTank in enemyTanks:
            # enemyTank.update(size, player1.rect.center)
    # for enemyTank in enemyTanks:
        # if not enemyTank.living:
            # enemyTanks.remove(enemyTank)
        # if len(enemyTanks) <= 0:
            # if lev < 10:
                # lev += 1
            # else:
                # lev = 1
            # blocks, player1.rect.center, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
            # for c in enemyTankCenters:
                # enemyTanks += [PlayerEnemy(3, c)]
                
                
    
    # screen.fill(bgColor)
    # screen.blit(bgPic, bgPicrect)
    # for enemyTank in enemyTanks:
        # screen.blit(enemyTank.image, enemyTank.rect)
        # screen.blit(enemyTank.turret.image, enemyTank.turret.rect)
    # if playerTank:
        # screen.blit(playerTank.image, playerTank.rect)
        # screen.blit(playerTurret.image, playerTurret.rect)
    # for block in blocks:
        # screen.blit(block.image, block.rect)
    # for bullet in bullets:
        # screen.blit(bullet.image, bullet.rect)
        
        
        
        
    all.update(size, player1.rect.center)
        
    playerHitBlocks = pygame.sprite.spritecollide(player1, blocks, False)
        
    
    for block in playerHitBlocks:
        player1.collide(block)    
    

    
    #screen.fill(bgColor)
    screen.blit(bgPic, bgPicrect)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
