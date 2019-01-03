import pygame, sys, math, random
import pygame, sys, math, random
from Tank import *
from PlayerTank import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1000
height = 800
size = width, height

screen = pygame.display.set_mode(size)

player1 = PlayerBall(5, [width/2, height/2])

bgColor = 0,0,0


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
   
    screen.fill(bgColor)
    screen.blit(player1.image, player1.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()
