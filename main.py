import pygame, time, math
from starship import Starship
from asteroid import Asteroid

# constants
WINDOW_SIZE = (860, 860)
BLACK = (0, 0, 0)
FPS = 60
START_TIME = time.monotonic()
T1_ASTEROID_SPAWN_PERIOD = 5
T2_ASTEROID_SPAWN_PERIOD = 7
T3_ASTEROID_SPAWN_PERIOD = 10
ROTATING_SPEED = 0.25
FLYING_SPEED = 0.01

# screen preparation
pygame.init()
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Asteroids')
last_time = time.monotonic()
spawn = True

# entities
player = Starship()
asteroids = []

running = True
while running:
    dt = time.monotonic() - last_time    
    last_time = time.monotonic()
    current_time = int(last_time - START_TIME + 1)  
    
    if current_time % T2_ASTEROID_SPAWN_PERIOD == 0:
        if spawn:
            asteroids.append(Asteroid(2))
            spawn = False
    elif current_time % T1_ASTEROID_SPAWN_PERIOD == 0:
        if spawn:
            asteroids.append(Asteroid(1))
            spawn = False
    else:
        spawn = True    

    SCREEN.fill(BLACK) 
    player.draw(SCREEN)
    for ast in asteroids:
        ast.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False          
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.runnig = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            player.runnig = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.dx += math.sin(math.radians(player.angle)) * -FLYING_SPEED * dt * FPS
        player.dy += math.cos(math.radians(player.angle)) * -FLYING_SPEED * dt * FPS
    if keys[pygame.K_d]:
        player.angle -= ROTATING_SPEED
        player.angle %= 360
    if keys[pygame.K_a]:
        player.angle += ROTATING_SPEED
        player.angle %= 360 
    
    player.update()   
    for ast in asteroids:
        ast.update()
    pygame.display.update()         

pygame.quit()   