import pygame


class Starship:
    def __init__(self):        
        self.image = [pygame.image.load('data/starship.png'), pygame.image.load('data/starship_running.png')]     
        self.runnig = 0
        self.pos = (470, 470)
        self.vel = (0, 0)

    def draw(self, screen):
        screen.blit(self.image[self.runnig], self.pos)