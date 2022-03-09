import pygame
from constants import *


class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 40)
        self.fps = self.clock.get_fps()        

    def draw(self, screen):
        self.fps = round(self.clock.get_fps(), 2)
        text = self.font.render(str(round(self.fps, 2)), True, WHITE)
        screen.blit(text, (0, 0))