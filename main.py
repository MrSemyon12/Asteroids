import pygame, time, math
from starship import Starship
from asteroid import Asteroid
from laser import Laser

# constants
WINDOW_SIZE = (860, 860)
BLACK = (0, 0, 0)
FPS = 60
START_TIME = time.monotonic()
T1_ASTEROID_SPAWN_PERIOD = 5
T2_ASTEROID_SPAWN_PERIOD = 7
T3_ASTEROID_SPAWN_PERIOD = 10
LASER_SPAWN_PERIOD = 100     
STARSHIP_ROTATING_SPEED = 5
STARSHIP_FLYING_SPEED = 0.01

# screen preparation
pygame.init()
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Asteroids')
last_time = time.monotonic()
spawn_asteroid = True
spawn_laser = True
ticks = 0

# entities
player = Starship()
asteroids = []
lasers = []

running = True
while running:
    ticks += 1
    ticks %= LASER_SPAWN_PERIOD
    dt = time.monotonic() - last_time    
    last_time = time.monotonic()
    current_time = int(last_time - START_TIME + 1)

    if current_time % T3_ASTEROID_SPAWN_PERIOD == 0:
        if spawn_asteroid:
            asteroids.append(Asteroid(3))
            spawn_asteroid = False
    elif current_time % T2_ASTEROID_SPAWN_PERIOD == 0:
        if spawn_asteroid:
            asteroids.append(Asteroid(2))
            spawn_asteroid = False    
    elif current_time % T1_ASTEROID_SPAWN_PERIOD == 0:
        if spawn_asteroid:
            asteroids.append(Asteroid(1))
            spawn_asteroid = False
    else:
        spawn_asteroid = True    

    SCREEN.fill(BLACK)     
    for ast in asteroids:
        ast.draw(SCREEN)
    for las in lasers:
        las.draw(SCREEN)
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
        player.dx += math.sin(math.radians(player.angle)) * -1 * STARSHIP_FLYING_SPEED * dt * FPS
        player.dy += math.cos(math.radians(player.angle)) * -1 * STARSHIP_FLYING_SPEED * dt * FPS
    if keys[pygame.K_d]:
        player.angle -= STARSHIP_ROTATING_SPEED * dt * FPS
        player.angle %= 360
    if keys[pygame.K_a]:
        player.angle += STARSHIP_ROTATING_SPEED * dt * FPS
        player.angle %= 360 
    if keys[pygame.K_SPACE]:  
        if (ticks % LASER_SPAWN_PERIOD == 0):  
            if spawn_laser:    
                lasers.append(Laser(player.x, player.y, player.angle))
                spawn_laser = False            
        else:
            spawn_laser = True
    
    player.update()   
    for ast in asteroids:
        ast.update()
    for las in lasers:
        las.update()
        if (las.x > 860 or las.x < 1 or las.y > 860 or las.y < 1):
            lasers.remove(las)   
    
    pygame.display.update()         

pygame.quit()
   