import pygame


class Starship:
    def __init__(self):
        self.pos = (400, 400)
        self.image = pygame.image.load('data/starship.png') 

    def draw(self, screen):
        screen.blit(self.image, self.pos)