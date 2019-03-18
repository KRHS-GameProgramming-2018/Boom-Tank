import pygame, sys, math, random
from TankBody import *
from PlayerTurret import *

class PlayerEnemy(Ball):
    def __init__(self, speed=5, startPos=[0,0]):
        self.imageE = pygame.image.load("EnemyTanks/Images/enemytankright.png")
        self.imageW = pygame.image.load("EnemyTanks/Images/enemytankleft.png")
        self.imageN = pygame.image.load("EnemyTanks/Images/enemytankup.png")
        self.imageS = pygame.image.load("EnemyTanks/Images/enemytankdown.png")
                       
        Ball.__init__(self, "PlayerTank/Images/tankup.png", [0,0], startPos)
        
        self.frame = 0;
        self.image = self.imageE
        self.rect = self.image.get_rect(center = startPos)
        
        self.maxspeed = speed
        self.goal = [0,0]
        self.tracking = True
        self.compass = 0
        self.directMove()
        
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.detectionRadius = 96
            
        self.living = True
        
        self.turret = PlayerTurret(speed, self.rect.center)
        
        
        self.lives = 1
        
    def setPos(self, pos):
        self.rect.center = pos
        
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
            
    def directMove(self, pCenter=None):
        if pCenter and self.getDist(pCenter) < 600:
            self.tracking = True
            xDif = abs(self.rect.centerx - pCenter[0])
            yDif = abs(self.rect.centery - pCenter[1])
            
            # print xDif, yDif, self.rect.center, pCenter
            
            if xDif > yDif:
                if self.rect.centerx < pCenter[0]:
                    self.compass = 1
                    print "Player Right"
                else:
                    self.compass = 3
                    print "Player Left"
            else:
                if self.rect.centery > pCenter[1]:
                    self.compass = 0
                    print "Player Above"
                else:
                    self.compass = 2
                    print "Player Below"
                
        else:
            if self.tracking: 
                self.tracking = False
                self.compass = random.randint(0, 3)
            elif random.randint (0, 60) == 0:
                self.compass = random.randint(0, 3)
                
        if self.compass == 0:
            self.moving = "Y"
            self.speedy = -self.maxspeed
            self.speedx = 0
            self.images = self.imageN
        elif self.compass == 1:
            self.moving = "X"
            self.speedx = self.maxspeed
            self.speedy = 0
            self.images = self.imageW
        elif self.compass == 2:
            self.moving = "Y"
            self.speedy = self.maxspeed
            self.speedx = 0
            self.images = self.imageS
        elif self.compass == 3:
            self.moving = "X"
            self.speedx = -self.maxspeed
            self.speedy = 0
            self.images = self.imageE
        # ~ self.image = self.images[self.frame]
        # ~ self.rect = self.image.get_rect()
            
        self.rect = self.rect.move(self.speed)
        
    def update(self, size, pCenter):
        # ~ print self.rect.center
        self.didBounceX = False
        self.didBounceY = False
        self.directMove(pCenter)
        self.move()
        
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            if not self.didBounceX:
                self.speedx = 0
                self.didBounceX = False
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = 0
                self.didBounceY = False   
        
    def collide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.top < other.rect.bottom:
                    if self.rect.bottom > other.rect.top:
                       
                        if not self.didBounceX:
                            if self.speedx > 1: #right
                                if self.rect.centerx < other.rect.centerx:
                                    self.speedx = -self.speedx
                                    self.move()
                                    self.tracking = True
                                    self.directMove()
                                    self.didBounceX = True
                                   
                            if self.speedx < 1: #left
                                if self.rect.centerx > other.rect.centerx:
                                    self.speedx = -self.speedx
                                    self.move()
                                    self.tracking = True
                                    self.directMove()
                                    self.didBounceX = True
                                    
                        if not self.didBounceY:
                            if self.speedy > 1: #down
                                if self.rect.centery < other.rect.centery:
                                    self.speedy = -self.speedy
                                    self.move()
                                    self.tracking = True
                                    self.directMove()
                                    self.didBounceY = True
                                    # ~ if self.rect.bottom > other.rect.top:
                                        # ~ self.rect.centery = other.rect.centery - ((self.rect.height)/2 + (other.rect.height)/2)

                            if self.speedy < 1: #up
                                if self.rect.centery > other.rect.centery:
                                    self.speedy  = -self.speedy
                                    self.move()
                                    self.tracking = True
                                    self.directMove()
                                    self.didBounceY = True
                                    # ~ if self.rect.top < other.rect.bottom:
                                        # ~ self.rect.centery = other.rect.centery + (self.rect.height)/2 + (other.rect.height)/2

                        return True
        return False
        
        
        
    def explode(self, bullet):
        if self.rect.right > bullet.rect.left:
            if self.rect.left < bullet.rect.right:
                if self.rect.top < bullet.rect.bottom:
                    if self.rect.bottom > bullet.rect.top:
                        #self.imageEX = pygame.image.load("PlayerTank/Images/tankright.png")
                        #self.imagePL = pygame.image.load("PlayerTank/Images/tankleft.png")
                        self.living = False
                        return True
                    
        return False
        
    def bounceBlock(self, other):
        if self.rect.left < other.rect.right or self.rect.right > other.rect.left:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
        if self.rect.top < other.rect.bottom or self.rect.bottom > other.rect.top:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True  
        
        
        
    
        
  
        
        
        
