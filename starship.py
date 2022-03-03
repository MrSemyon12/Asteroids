import pygame


class Starship:
    def __init__(self):        
        self.image = [pygame.image.load('data/starship.png'), pygame.image.load('data/starship_running.png')]     
        self.runnig = 0
        self.x = 430
        self.y = 430       
        self.angle = 0        
        self.dx = 0
        self.dy = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if (self.x > 860):
            self.x = 1
        if (self.y > 860):
            self.y = 1
        if (self.x < 1):
            self.x = 860
        if (self.y < 1):
            self.y = 860

    def draw(self, screen):
        img_copy = pygame.transform.rotate(self.image[self.runnig], self.angle)
        screen.blit(img_copy, (self.x - int(img_copy.get_width() / 2), self.y - int(img_copy.get_height() / 2)))   
       