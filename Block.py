import pygame, sys, math

class Block(pygame.sprite.Sprite):
    def __init__(self, pos=[6,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("block.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

