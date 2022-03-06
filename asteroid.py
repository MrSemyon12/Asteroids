import pygame, random


image = [pygame.image.load('data/asteroid_t1.png'),
         pygame.image.load('data/asteroid_t2.png'),
         pygame.image.load('data/asteroid_t3.png')]

class Asteroid:
    def __init__(self, tier):
        self.tier = tier
        self.image = image[tier - 1]
        self.hp = tier * 2

        if (random.randint(0, 1)):
            if (random.randint(0, 1)):
                self.x = 1                
            else:
                self.x = 860
            self.y = random.randint(1, 860)
        else:
            if (random.randint(0, 1)):
                self.y = 1                
            else:
                self.y = 860
            self.x = random.randint(1, 860)
              
        self.angle = random.randint(1, 180)
        self.dangle = random.uniform(-0.3, 0.3) / tier
        self.dx = random.uniform(-0.3, 0.3) / tier
        self.dy = random.uniform(-0.3, 0.3) / tier

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.angle += self.dangle

        if (self.x > 860):
            self.x = 1
        if (self.y > 860):
            self.y = 1
        if (self.x < 1):
            self.x = 860
        if (self.y < 1):
            self.y = 860

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))
        #screen.blit(self.image, (self.x - int(self.image.get_width() / 2), self.y - int(self.image.get_height() / 2)))
        