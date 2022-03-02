import pygame, time
from starship import Starship

# screen settings
pygame.init()
WINDOW_SIZE = (980, 980)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Asteroids')
last_time = time.time()

# entities
player = Starship()

while True:
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    SCREEN.fill((0, 0, 0))
    player.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.runnig = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            player.runnig = 0


    pygame.display.update() 
    