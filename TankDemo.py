import pygame, sys, math, random
from Ball import *
from PlayerBall import *
from Level import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

level = loadLevel("Levels/1.lvl")

balls = []

for i in range(3):
    images = ["Images/Ball/ball.png"]
    speed = [random.randint(1,10), random.randint(1,10)]
    pos = [random.randint(0,690), random.randint(0,690)]
    balls += [Ball(images[0], speed, pos)]

player1 = PlayerBall(5, [width/2, height/2])

bgColor = 0,0,0

mposX = 0
mposY = 0

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.go("up")
            if event.key == pygame.K_a:
                player1.go("left")
            if event.key == pygame.K_s:
                player1.go("down")
            if event.key == pygame.K_d:
                player1.go("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.go("sup")
            if event.key == pygame.K_a:
                player1.go("sleft")
            if event.key == pygame.K_s:
                player1.go("sdown")
            if event.key == pygame.K_d:
                player1.go("sright")
            
    for ball in balls:
        ball.update(size)
    player1.update(size)
        
    for hitter in balls:
        for hittie in balls:
            hitter.collide(hittie)
        for tile in level:
            hitter.collide(tile)
        hitter.collide(player1)
        player1.collide(hitter)
        for Block in level:
            player1.collide(Block)
             
            

    
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for tile in level:
        screen.blit(tile.image, tile.rect)
    screen.blit(player1.image, player1.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()
