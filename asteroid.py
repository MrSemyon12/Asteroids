import pygame, random
from constants import *


image = [pygame.image.load('data/asteroid_t1.png'),
         pygame.image.load('data/asteroid_t2.png'),
         pygame.image.load('data/asteroid_t3.png')]

class Asteroid:
    def __init__(self, tier):
        self.tier = tier
        self.image = image[tier - 1]
        self.hp = tier * 2
        self.mangle = random.uniform(-ASTEROID_ROTATING_SPEED, ASTEROID_ROTATING_SPEED) / tier
        self.mx = random.uniform(-ASTEROID_FLYING_SPEED, ASTEROID_FLYING_SPEED) / tier
        self.my = random.uniform(-ASTEROID_FLYING_SPEED, ASTEROID_FLYING_SPEED) / tier

        if (random.randint(0, 1)):
            if (random.randint(0, 1)):
                self.x = 1                
            else:
                self.x = WINDOW_SIZE[0]
            self.y = random.randint(1, WINDOW_SIZE[1])
        else:
            if (random.randint(0, 1)):
                self.y = 1                
            else:
                self.y = WINDOW_SIZE[1]
            self.x = random.randint(1, WINDOW_SIZE[0])
              
        self.angle = random.randint(1, 180)
        self.dangle = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.angle += self.dangle

        if (self.x > WINDOW_SIZE[0]):
            self.x = 0
        if (self.y > WINDOW_SIZE[1]):
            self.y = 0
        if (self.x < 0):
            self.x = WINDOW_SIZE[0]
        if (self.y < 0):
            self.y = WINDOW_SIZE[1]

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))        
        