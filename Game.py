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
tanks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Block.containers = (blocks, all)
Turret.containers = (tanks, all)
TankBody.containers = (tanks, all)
PlayerTankBody.containers = (playerTanks, all)
EnemyTank.containers = (enemyTanks, all)
Bullet.containers = (bullets, all)







bgColor = 0,0,0

bgPic = pygame.image.load("wood.png")
bgPicrect = bgPic.get_rect()

lev=1
pcenter, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
player1 = PlayerTankBody(3, pcenter)


for c in enemyTankCenters:
    EnemyTank(3, c)
    
        
mposX = 0
mposY = 0
#raw_input("> ");

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
        
    if len(enemyTanks.sprites()) <= 0:
        print "No Tanks"
        if lev < 10:
            lev += 1
        else:
            lev == 1
            
        for s in all.sprites():
            s.kill()
        pcenter, enemyTankCenters = loadLevel("Levels/"+str(lev)+".lvl")
        player1 = PlayerTankBody(3, pcenter)

        for c in enemyTankCenters:
            EnemyTank(3, c)        
            
    playerHitBlocks = pygame.sprite.spritecollide(player1, blocks, False)
    for block in playerHitBlocks:
        player1.collide(block) 
        
    playerHitEnemys = pygame.sprite.spritecollide(player1, enemyTanks, False, pygame.sprite.collide_mask)
    if len(playerHitEnemys) > 0:
        player1.kill()
        
    enemyTanksHitBlocks = pygame.sprite.groupcollide(enemyTanks, blocks, False, False)
    for enemy in enemyTanksHitBlocks:
        for block in enemyTanksHitBlocks[enemy]:
            enemy.collide(block)
    
    enemyTanksHitBullets = pygame.sprite.groupcollide(enemyTanks, bullets, True, True)
   
    """
    print "all.sprites():"
    for s in all.sprites():
        print "\t", s
    print "all.spritedict.keys():"
    for s in all.spritedict.keys():
        print "\t",s, all.spritedict[s]
    """        
    bulletsHitBlocks = pygame.sprite.groupcollide(bullets, blocks, True, False)

    all.update(size, player1.rect.center)
    
    
    screen.blit(bgPic, bgPicrect)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
