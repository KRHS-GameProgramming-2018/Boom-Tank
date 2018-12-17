import pygame, sys, math
from tank import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed, startPos=[0,0]):
        self.baseImage = pygame.image.load("turret.png")
        
        Ball.__init__(self, "turret.png", [0,0], startPos)
        
        
        self.angle = 0
        self.image = pygame.transform.rotate(self.baseImage, 0)
        self.rect = self.image.get_rect(center = startPos)
        
        self.maxSpeed = maxSpeed
        self.goal = [0,0]
        
    def setPos(self, pos):
        self.rect.center = pos
        
    def go(self, d):
        if d == "up":
            self.speedy = -self.maxSpeed
            self.images = self.imagesN
        if d == "down":
            self.speedy = self.maxSpeed
            self.images = self.imagesS
        if d == "left":
            self.speedx = -self.maxSpeed
            self.images = self.imagesW
        if d == "right":
            self.speedx = self.maxSpeed
            self.images = self.imagesE
            
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

    def rotate(self, point):
        mousePos = pygame.mouse.get_pos()
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        self.angle = -self.angle
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
