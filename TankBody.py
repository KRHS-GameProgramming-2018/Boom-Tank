import pygame, sys, math


class TankBody(pygame.sprite.Sprite):
    def __init__(self, image, speed=[5,5], startPos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
            
    def update(*args):
        self = args[0]
        size = args[1]
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            if not self.didBounceX:
                self.speedx = -self.speedx
                self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True
            
    def collide(self, other):
        if not(self == other):
            if not self.didBounceX:
                if self.speedx > 1: #right
                    if self.rect.centerx < other.rect.centerx:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                if self.speedx < 1: #left
                    if self.rect.centerx > other.rect.centerx:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                        
            if not self.didBounceY:
                if self.speedy > 1: #down
                    if self.rect.centery < other.rect.centery:
                        self.speedy = -self.speedy
                        self.didBounceY = True
                if self.speedy < 1: #up
                    if self.rect.centery > other.rect.centery:
                        self.speedy  = -self.speedy
                        self.didBounceY = True
            return True
        return False
