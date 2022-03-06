import pygame
from constants import *


class Starship:
    def __init__(self, window_size):        
        self.image = [pygame.image.load('data/starship.png'), pygame.image.load('data/starship_running.png')]     
        self.runnig = 0
        self.x = window_size[0] // 2
        self.y = window_size[1] // 2         
        self.mx = 0
        self.my = 0    
        self.angle = 0                
        self.dx = 0
        self.dy = 0
        self.max_x = window_size[0]
        self.max_y = window_size[1]

    def update(self):
        self.x += self.dx
        self.y += self.dy     

        if (self.x > self.max_x):
            self.x = 0
        if (self.y > self.max_y):
            self.y = 0
        if (self.x < 0):
            self.x = self.max_x
        if (self.y < 0):
            self.y = self.max_y

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image[self.runnig], self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))   
       