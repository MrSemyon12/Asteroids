import pygame, random
from constants import *


class Asteroid:
    def __init__(self, tier, window_size, image, x = 0, y = 0):
        self.tier = tier
        self.image = image[tier - 1]
        self.mask = pygame.mask.from_surface(self.image)        
        self.mangle = random.uniform(-ASTEROID_ROTATING_SPEED, ASTEROID_ROTATING_SPEED) / tier
        self.mx = random.uniform(-ASTEROID_FLYING_SPEED, ASTEROID_FLYING_SPEED) / tier
        self.my = random.uniform(-ASTEROID_FLYING_SPEED, ASTEROID_FLYING_SPEED) / tier
        self.max_x = window_size[0] + int(self.image.get_width() / 2)
        self.max_y = window_size[1] + int(self.image.get_height() / 2)
        self.min_x = int(-self.image.get_width() / 2)
        self.min_y = int(-self.image.get_height() / 2)

        if x + y == 0:
            if (random.randint(0, 1)):
                if (random.randint(0, 1)):
                    self.x = self.min_x                
                else:
                    self.x = self.max_x
                self.y = random.randint(self.min_y, self.max_y)
            else:
                if (random.randint(0, 1)):
                    self.y = self.min_y                
                else:
                    self.y = self.max_y
                self.x = random.randint(self.min_x, self.max_x)
        else:
            self.x = x
            self.y = y
              
        self.angle = random.randint(1, 180)
        self.dangle = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.angle += self.dangle

        if (self.x > self.max_x):
            self.x = self.min_x
        if (self.y > self.max_y):
            self.y = self.min_y
        if (self.x < self.min_x):
            self.x = self.max_x
        if (self.y < self.min_y):
            self.y = self.max_y

        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))          
        