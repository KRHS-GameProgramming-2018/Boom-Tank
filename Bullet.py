import pygame, sys, math, random
from PlayerTurret import *
from PlayerTankBody import*

class Bullet(Ball):
    def __init__(self, image="PlayerTank/Images/Ball.png", speed=10, startPos=[0,0]):
        #PlayerTurret.__init__(self,  image, speed, startPos)
        self.baseImage = pygame.image.load("PlayerTank/Images/Ball.png")
        
       
        Ball.__init__(self, "PlayerTank/Images/Ball.png", [0,0], startPos)
        # ~ print self.rect.center, speed
        self.kind = "bullet"
        self.lives = 1
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                        if self.radius + other.radius > self.getDist(other.rect.center):
                            self.alive = False
        return False
