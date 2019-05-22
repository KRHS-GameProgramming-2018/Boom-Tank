import pygame, sys, math
from TankBody import *
from PlayerTurret import *

class PlayerTankBody(TankBody):
    def __init__(self, maxSpeed, startPos=[550,-100]):
        self.imageE = pygame.image.load("PlayerTank/Images/tankright.png")
        self.imageW = pygame.image.load("PlayerTank/Images/tankleft.png")
        self.imageN = pygame.image.load("PlayerTank/Images/tankup.png")
        self.imageS = pygame.image.load("PlayerTank/Images/tankdown.png")
                       
        TankBody.__init__(self, "PlayerTank/Images/tankup.png", [0,0], [500,500])
        
        self.frame = 0;
        self.image = self.imageE
        self.rect = self.image.get_rect(center = startPos)
        
        self.moveSound = pygame.mixer.Sound("PlayerTank/Sounds/moving.wav")
        self.moving = False;
        self.playingMoving = False
        
        self.turret = PlayerTurret(maxSpeed, self.rect.center)

        self.living = True
        
        self.lives = 1
        
        self.maxSpeed = maxSpeed
        self.goal = [0,0]
        
        self.living = True
        
        
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
            
    def update(*args):
        self = args[0]
        size = args[1]
        if self.speed != [0,0]:
            self.moving = True
        else:
            self.moving = False
        
        if self.moving and not self.playingMoving:
            self.moveSound.play(-1);
            self.playingMoving = True;
        elif not self.moving and self.playingMoving:
            self.moveSound.fadeout(500);
            self.playingMoving = False;
            
        self.turret.rect.center = self.rect.center
        TankBody.update(self, size)
        
        
        
    
    
    #def update(self, size):
        # if self.speed != [0,0]:
            # self.moving = True
        # else:
            # self.moving = False
        
        # if self.moving and not self.playingMoving:
            # self.moveSound.play(-1);
            # self.playingMoving = True;
        # elif not self.moving and self.playingMoving:
            # self.moveSound.fadeout(500);
            # self.playingMoving = False;
            
        # Ball.update(self, size)
        
        
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
            
        #print self.speedx, self.speedy
            
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
                self.speedx = 0
                self.didBounceX = False
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = 0
                self.didBounceY = False   
        
    def collide(self, other):
        #print "hit"
        if not(self == other):
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
                   self.didBounceY = True

            return True
        return False

    

    def kill(self):
        self.turret.kill()
        pygame.sprite.Sprite.kill(self)    
        
    def explode(self, bullet):
        if self.rect.right > bullet.rect.left:
            if self.rect.left < bullet.rect.right:
                if self.rect.top < bullet.rect.bottom:
                    if self.rect.bottom > bullet.rect.top:
                        self.imageEX = pygame.image.load("PlayerTank/Images/tankright.png")
                        self.imagePL = pygame.image.load("PlayerTank/Images/tankleft.png")
                        self.living = False
                        return True
                        
        return False
        

