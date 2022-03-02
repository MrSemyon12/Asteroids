import pygame


image = [pygame.image.load('data/asteroid_t1.png')]

class Asteroid:
    def __init__(self, tier):
        self.tier = tier
        self.image = image[tier - 1]
        self.hp = tier * 2
        self.x = 200
        self.y = 600       
        self.angle = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if (self.x > 980):
            self.x = 1
        if (self.y > 980):
            self.y = 1
        if (self.x <= 0):
            self.x = 980
        if (self.y <= 0):
            self.y = 980

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image, self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))