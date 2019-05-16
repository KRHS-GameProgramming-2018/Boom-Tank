import pygame, sys, math, random
import pygame, sys, math, random          
from Turret import *
from PlayerTurret import *
from PlayerTankBody import *
from Levels import *
from EnemyTank import *
from Bullet import *
from TankBody import *
from background import *
from Button import *
from EnemyTurret import *

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
tanks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
buttons = pygame.sprite.Group()

all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, all)
Turret.containers = (tanks, all)
TankBody.containers = (tanks, all)
PlayerTankBody.containers = (playerTanks, all)
EnemyTank.containers = (enemyTanks, all)
Bullet.containers = (bullets, all)
Background.containers = (all)
Button.containers = (all, buttons)



mode = "ready"
while True:
    bg = Background ("Images/Screens/boomStartScreen.png")
    startButton = Button ("start",[500,375])
    while mode == "ready":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #mode = "play"
                if event.key == pygame.K_ESCAPE:
                    mode = "menu"
                if event.type == pygame.QUIT:
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 0:
                    startButton.checkHover(event.pos)
                else:
                    startButton.checkClick(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    startButton.checkClick(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.collidePt(event.pos):
                    mode = "play"
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    
    bg.kill()
    lev = 1
    bg = Background("wood.png")
    pcenter, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
    player1 = PlayerTankBody(3, pcenter)
    for c in enemyTankCenters:
        EnemyTank(3, c)
    while mode == "play":
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
            
        if len(enemyTanks.sprites()) <= 0:
            if lev < 10:
                lev += 1
                print "next"
            if lev == 10:
                mode = "win"
                
                
            for s in all.sprites():
                s.kill()
            bg = Background("wood.png")
            pcenter, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
            player1 = PlayerTankBody(3, pcenter)

            for c in enemyTankCenters:
                EnemyTank(3, c)   
                
                
        if len(playerTanks.sprites()) <= 0:
            mode = "death"
            for s in all.sprites():
                s.kill()
                
                
        playerHitBlocks = pygame.sprite.spritecollide(player1, blocks, False, False)
        for block in playerHitBlocks:
            player1.collide(block) 
            
        
            
        playerHitEnemys = pygame.sprite.spritecollide(player1, enemyTanks, False, False)
        if len(playerHitEnemys) > 0:
            player1.kill()
         
        enemyTanksHitBlocks = pygame.sprite.groupcollide(enemyTanks, blocks, False, False)
        for enemy in enemyTanksHitBlocks:
            for block in enemyTanksHitBlocks[enemy]:
                enemy.collide(block)

        enemyTanksHitBullets = pygame.sprite.groupcollide(enemyTanks, bullets, True, True)
        # for EnemyTank in enemytanks:
            # if bullet.collide(Enemytank):
                # pygame.transform.scale(pygame.image.load("PlayerTank/Images/explosion.png"),


        bulletsHitBlocks = pygame.sprite.groupcollide(bullets, blocks, True, False)

        all.update(size, player1.rect.center)


        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip( )
        clock.tick(60)
                
    bg.kill()
    bg = Background("PlayerTank/Images/DEATHSCREEN.png")         
    while mode == "death":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for s in all.sprites():
                    s.kill()
                    if event.key == pygame.K_SPACE:
                        mode = "ready"
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    
    bg.kill()            
    
    while mode == "win":
        bg = Background("Images/Screens/win.png")
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for s in all.sprites():
                    s.kill()
                    if event.key == pygame.K_SPACE:
                        mode = "ready"
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    
    bg.kill()            
    
    while mode == "war zone":
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
