import pygame, sys, math, random

class bullet:
    def __init__(self, angle, startPos=[0,0]):
         self.image = [pygame.image.load("PlayerTank/Images/Ball.png")],
      
        
         bullet.__init__(self, angle, [0,0])
        
         self.frame = 0;
         self.image = self.image[self.frame]
         self.rect = self.image.get_rect()
        
         self.maxSpeed = maxSpeed
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
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = False
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = False   
        
    def collide(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                if not self.didBounceX:
                                    if self.speedx > 1: #right
                                        if self.rect.centerx < other.rect.centerx:
                                            self.speedx = 0
                                            self.didBounceX = True
                                    if self.speedx < 1: #left
                                        if self.rect.centerx > other.rect.centerx:
                                            self.speedx = 0
                                            self.didBounceX = True
                                            
                                if not self.didBounceY:
                                    if self.speedy > 1: #down
                                        if self.rect.centery < other.rect.centery:
                                            self.speedy = 0
                                            self.didBounceY = True
                                    if self.speedy < 1: #up
                                        if self.rect.centery > other.rect.centery:
                                            self.speedy  = 0
                                            self.didBounceY = True

                                return True
        return False
    
    
