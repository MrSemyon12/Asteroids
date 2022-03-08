import pygame, time, math
from starship import Starship
from asteroid import Asteroid
from laser import Laser
from constants import *

# Setup ----------------------------------------------------------- #
pygame.init()
pygame.display.set_caption('Asteroids')
window_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
screen = pygame.display.set_mode(window_size, flags, 8)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
#window_size = (800, 800)
#screen = pygame.display.set_mode(window_size, 0, 32)

last_time = start_time = time.time()
last_second = 0
last_msecond = 0
spawn_asteroid = 1
spawn_laser = 1
running = 1
hard_lvl = 1
lvl_up = 1

# Images ---------------------------------------------------------- #
asteroid_image = [pygame.image.load('data/asteroid_t1.png').convert_alpha(),
                  pygame.image.load('data/asteroid_t2.png').convert_alpha(),
                  pygame.image.load('data/asteroid_t3.png').convert_alpha()]
starship_image = [pygame.image.load('data/starship.png').convert_alpha(), 
                  pygame.image.load('data/starship_running.png').convert_alpha()]
laser_image =     pygame.image.load('data/laser.png').convert_alpha()

# Entities -------------------------------------------------------- #
starship = Starship(window_size, starship_image)
asteroids = []
lasers = []

# Main loop ------------------------------------------------------- #
while running:      
    current_time = time.time()
    dt = (current_time - last_time) * FPS   
    second = last_time - start_time + 1
    msecond = int(math.modf(second)[0] * 100)
    second = int(second)    
    last_time = current_time    

    if last_second != second:
        spawn_asteroid = 1
        last_second = second 

    if last_msecond != msecond:
        spawn_laser = 1
        last_msecond = msecond   

    if second % HARD_LVL_UP_PERIOD == 0:
        if lvl_up:
            hard_lvl += 1
            lvl_up = 0
    else: lvl_up = 1
    
    if spawn_asteroid:
        if second % ASTEROID_T3_SPAWN_PERIOD == 0:  
            for i in range(hard_lvl):          
                asteroids.append(Asteroid(3, window_size, asteroid_image))
                asteroids.append(Asteroid(3, window_size, asteroid_image))
                asteroids.append(Asteroid(3, window_size, asteroid_image))                
            spawn_asteroid = 0
        elif second % ASTEROID_T2_SPAWN_PERIOD == 0: 
            for i in range(hard_lvl):
                asteroids.append(Asteroid(2, window_size, asteroid_image))
                asteroids.append(Asteroid(2, window_size, asteroid_image))                           
            spawn_asteroid = 0                  
    
    # Drawing ----------------------------------------------------- #    
    screen.fill(BLACK)
    for ast in asteroids:
        ast.draw(screen)
    for las in lasers:
        las.draw(screen)
    starship.draw(screen)    

    # Buttons ----------------------------------------------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = 0          
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
                laser = Laser(starship.x, starship.y, starship.angle, laser_image)
                laser.mx = math.sin(math.radians(laser.angle)) * -1 * LASER_FLYING_SPEED
                laser.my = math.cos(math.radians(laser.angle)) * -1 * LASER_FLYING_SPEED  
                lasers.append(laser)
                spawn_laser = 0            
            
    # Update and collide ------------------------------------------ #  
    for ast in asteroids:
        ast.dx = ast.mx * dt
        ast.dy = ast.my * dt
        ast.dangle = ast.mangle * dt        
        ast.update()
        if starship.collide(ast.mask, ast.x, ast.y) != None:            
            starship.health -= 1        

    for las in lasers:
        las.dx = las.mx * dt
        las.dy = las.my * dt 
        las.update()
        if (las.x > window_size[0] + 100 or las.x < -100 or las.y > window_size[1] + 100 or las.y < -100):
            lasers.remove(las) 
        for ast in asteroids:
            if las.collide(ast.mask, ast.x, ast.y) != None:
                if ast.tier > 1:
                    asteroids.append(Asteroid(ast.tier - 1, window_size, asteroid_image, ast.x, ast.y))
                    asteroids.append(Asteroid(ast.tier - 1, window_size, asteroid_image, ast.x, ast.y))
                asteroids.remove(ast)
                if las in lasers:
                    lasers.remove(las)

    starship.dx = starship.mx * dt
    starship.dy = starship.my * dt
    starship.update()    
    
    pygame.display.update()    

pygame.quit()
