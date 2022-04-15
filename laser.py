import pygame
from constants import *

class Laser:
    def __init__(self, x, y, angle, image):        
        self.image = image        
        self.x = x
        self.y = y   
        self.mx = 0 
        self.my = 0   
        self.angle = angle        
        self.dx = 0
        self.dy = 0        

    def collide(self, mask, x, y):
        laser_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.x - x), int(self.y - y))
        is_collide = mask.overlap(laser_mask, offset)
        return is_collide

    def update(self):
        self.x += self.dx
        self.y += self.dy        

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))
        