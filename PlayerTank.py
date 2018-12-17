import pygame, sys, math
from tank import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed, startPos=[0,0]):
        self.baseImage = pygame.image.load("turret.png")
        
        Ball.__init__(self, "turret.png", [0,0], startPos)
        
        
        self.angle = 0
        self.image = pygame.transform.rotate(self.baseImage, 0)
        self.rect = self.image.get_rect(center = startPos)
        
        s
        elf.maxSpeed = maxSpeed
        self.goal = [0,0]
        
    def setPos(self, pos):
        self.rect.center = pos
        
   
            
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

    def rotate(self, point):
        c = self.rect.center
        
        self.angle = 270
        self.image = pygame.transform.rotate(self.baseImage, self.angle)
        self.rect = self.image.get_rect(center = c)

