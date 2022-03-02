import pygame, time, math
from starship import Starship

# constants
WINDOW_SIZE = (980, 980)
BLACK = (0, 0, 0)

# screen settings
pygame.init()
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Asteroids')
last_time = time.time()

# entities
player = Starship()

running = True
while running:
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()

    SCREEN.fill(BLACK) 
    player.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False          
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.runnig = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            player.runnig = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.dx += math.sin(math.radians(player.angle)) * -0.01 * dt
        player.dy += math.cos(math.radians(player.angle)) * -0.01 * dt   
    if keys[pygame.K_d]:
        player.angle -= 0.25
        player.angle %= 360
    if keys[pygame.K_a]:
        player.angle += 0.25
        player.angle %= 360 

    player.update()    
    pygame.display.update()      

pygame.quit()   