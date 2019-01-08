import pygame, sys, math
from TankBody import *

class PlayerTankBody(Ball):
    def __init__(self, maxSpeed, startPos=[0,0]):
        self.imageE = pygame.image.load("PlayerTank/Images/tankright.png")
        self.imageW = pygame.image.load("PlayerTank/Images/tankleft.png")
        self.imageN = pygame.image.load("PlayerTank/Images/tankup.png")
        self.imageS = pygame.image.load("PlayerTank/Images/tankdown.png")
                       
        Ball.__init__(self, "PlayerTank/Images/tankup.png", [0,0], startPos)
        
        self.frame = 0;
        self.image = self.imageE
        self.rect = self.image.get_rect()
            
        
        self.maxSpeed = maxSpeed
        self.goal = [0,0]
        
    def setPos(self, pos):
        self.rect.center = pos
        
    def go(self, d):
        if d == "up":
            self.speedy = -self.maxSpeed
            self.image = self.imageN
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
            
    def update(self, size):
        Ball.update(self, size)
        
        
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
            
        print self.speedx, self.speedy
            
    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        

