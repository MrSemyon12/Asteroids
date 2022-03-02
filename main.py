import pygame, time
from starship import Starship

pygame.init()
WINDOW_SIZE = (980, 980)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Asteroids')
last_time = time.time()
player = Starship()

while True:
    dt = time.time() - last_time
    last_time = time.time()

    SCREEN.fill((0, 0, 0))
    player.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()        

    pygame.display.update() 
    