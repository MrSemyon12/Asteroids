import pygame, math
from constants import *


class Laser:
    def __init__(self, x, y, angle):        
        self.image = pygame.image.load('data/laser.png')        
        self.x = x
        self.y = y   
        self.mx = 0 
        self.my = 0   
        self.angle = angle        
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy        

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))
        