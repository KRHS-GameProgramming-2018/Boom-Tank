import pygame, sys, math

class Block:
    def __init__(self, pos=[6,0]):
        self.image = pygame.image.load("block.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

