import pygame, random
from constants import *


image = [pygame.image.load('data/asteroid_t1.png'),
         pygame.image.load('data/asteroid_t2.png'),
         pygame.image.load('data/asteroid_t3.png')]

class Asteroid:
    def __init__(self, tier, window_size):
        self.tier = tier
        self.image = image[tier - 1]
        self.hp = tier * 2
        self.mangle = random.uniform(-ASTEROID_ROTATING_SPEED, ASTEROID_ROTATING_SPEED) / tier
        self.mx = random.uniform(-ASTEROID_FLYING_SPEED, ASTEROID_FLYING_SPEED) / tier
        self.my = random.uniform(-ASTEROID_FLYING_SPEED, ASTEROID_FLYING_SPEED) / tier
        self.max_x = window_size[0]
        self.max_y = window_size[1]

        if (random.randint(0, 1)):
            if (random.randint(0, 1)):
                self.x = 0                
            else:
                self.x = self.max_x
            self.y = random.randint(0, self.max_y)
        else:
            if (random.randint(0, 1)):
                self.y = 0                
            else:
                self.y = self.max_y
            self.x = random.randint(0, self.max_x)
              
        self.angle = random.randint(1, 180)
        self.dangle = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.angle += self.dangle

        if (self.x > self.max_x):
            self.x = 0
        if (self.y > self.max_y):
            self.y = 0
        if (self.x < 0):
            self.x = self.max_x
        if (self.y < 0):
            self.y = self.max_y

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))        
        