import pygame, time, math
from starship import Starship
from asteroid import Asteroid
from laser import Laser
from constants import *

# Setup pygame/window --------------------------------------------- #
pygame.init()
pygame.display.set_caption('Asteroids')
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

last_time = start_time = time.time()
last_second = 0
last_msecond = 0
spawn_asteroid = True
spawn_laser = True
running = True

# Entities -------------------------------------------------------- #
starship = Starship()
asteroids = []
lasers = []

# Main loop ------------------------------------------------------- #
while running:      
    current_time = time.time()
    dt = (current_time - last_time) * FPS   
    second = last_time - start_time + 1
    msecond = int(math.modf(second)[0] * 10)
    second = int(second)    
    last_time = current_time    

    if last_second != second:
        spawn_asteroid = True
        last_second = second 

    if last_msecond != msecond:
        spawn_laser = True
        last_msecond = msecond   
    
    if spawn_asteroid:
        if second % ASTEROID_T3_SPAWN_PERIOD == 0:            
            asteroids.append(Asteroid(3))
            spawn_asteroid = False
        elif second % ASTEROID_T2_SPAWN_PERIOD == 0:            
            asteroids.append(Asteroid(2))
            spawn_asteroid = False    
        elif second % ASTEROID_T1_SPAWN_PERIOD == 0:
            asteroids.append(Asteroid(1))
            spawn_asteroid = False           

    screen.fill(BLACK)     
    for ast in asteroids:
        ast.draw(screen)
    for las in lasers:
        las.draw(screen)
    starship.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False          
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            starship.runnig = 1
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            starship.runnig = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        starship.mx += math.sin(math.radians(starship.angle)) * -1 * STARSHIP_FLYING_SPEED * dt
        starship.my += math.cos(math.radians(starship.angle)) * -1 * STARSHIP_FLYING_SPEED * dt     
    if keys[pygame.K_d]:
        starship.angle -= STARSHIP_ROTATING_SPEED * dt
        starship.angle %= 360
    if keys[pygame.K_a]:
        starship.angle += STARSHIP_ROTATING_SPEED * dt
        starship.angle %= 360
    if keys[pygame.K_SPACE]: 
        if spawn_laser: 
            if (msecond % LASER_SPAWN_PERIOD == 0):            
                laser = Laser(starship.x, starship.y, starship.angle)
                laser.mx = math.sin(math.radians(laser.angle)) * -1 * LASER_FLYING_SPEED
                laser.my = math.cos(math.radians(laser.angle)) * -1 * LASER_FLYING_SPEED  
                lasers.append(laser)
                spawn_laser = False            
            
    # Update ------------------------------------------------------ #  
    for ast in asteroids:
        ast.dx = ast.mx * dt
        ast.dy = ast.my * dt
        ast.dangle = ast.mangle * dt        
        ast.update()
    for las in lasers:
        las.dx = las.mx * dt
        las.dy = las.my * dt 
        las.update()
        if (las.x > WINDOW_SIZE[0] or las.x < 0 or las.y > WINDOW_SIZE[1] or las.y < 0):
            lasers.remove(las)          
    starship.dx = starship.mx * dt
    starship.dy = starship.my * dt
    starship.update()

    pygame.display.update()    

pygame.quit()
