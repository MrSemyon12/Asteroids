import pygame, random

class Particle:
    def __init__(self, x, y, color):               
        self.x = x
        self.y = y             
        self.color = color 
        self.radius = random.randint(1, 5) 
        self.timer = random.randint(10, 100)    
        self.dx = random.randint(-100, 100) / 10
        self.dy = random.randint(-100, 100) / 10      
   
    def update(self):
        self.x += self.dx
        self.y += self.dy 
        self.timer -= 1       

    def draw(self, screen):        
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        