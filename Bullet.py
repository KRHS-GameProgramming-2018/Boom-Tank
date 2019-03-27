import pygame, sys, math, random
from PlayerTurret import *

class Bullet(Turret):
    def __init__(self, angle=0, startPos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)

        #PlayerTurret.__init__(self,  image, speed, startPos)
        self.baseImage = pygame.image.load("PlayerTank/Images/Ball.png")
        
       
        Turret.__init__(self, "PlayerTank/Images/Ball.png", [0,0], startPos)
        # ~ print self.rect.center, speed
        self.kind = "bullet"
        self.living = True
        self.maxSpeed = 10
        self.didBounceY = False   

        
        #print angle
        
        self.speedx = self.maxSpeed*math.cos(math.radians(angle))
        self.speedy = -self.maxSpeed*math.sin(math.radians(angle))
        self.speed = [self.speedx, self.speedy]
        
        
    def headTo(self, pos):
        self.goal = pos
        if self.rect.centerx > pos[0]:
            self.speedx = -self.maxSpeed
        elif self.rect.centerx < pos[0]:
            self.speedx = self.maxSpeed
        else:
            self.speedx = 0
            
        if self.rect.centery > pos[1]:
            self.speedy = -self.maxSpeed
        elif self.rect.centery < pos[1]:
            self.speedy = self.maxSpeed
        else:
            self.speedy = 0
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def go(self, d):
        d =  mousePosPlayerX, mousePosPlayerY 
        if d == "up":
            self.speedy = -self.maxSpeed
        if d == "down":
            self.speedy = self.maxSpeed
            self.image = self.imageS
        if d == "left":
            self.speedx = -self.maxSpeed
            self.image = self.imageW
        if d == "right":
            self.speedx = self.maxSpeed
            self.image = self.imageE
            
        if d == "sup":
            self.speedy = 0
        if d == "sdown":
            self.speedy = 0
        if d == "sleft":
            self.speedx = 0
        if d == "sright":
            self.speedx = 0
            
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.living = False
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.living = False   
        
        
    def collide(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                self.living = False
                                return True
        return False
