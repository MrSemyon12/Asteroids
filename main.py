import pygame, time, math, random, sys
from starship import Starship
from asteroid import Asteroid
from laser import Laser
from fps import FPS
from constants import *


# Setup ----------------------------------------------------------- #
pygame.init()
pygame.display.set_caption('Asteroids')
pygame.display.set_icon(pygame.image.load('data/asteroid_t1.png'))
# window_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
window_size = (1200, 900)
flags = pygame.DOUBLEBUF
screen = pygame.display.set_mode(window_size, flags, 32)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
fps = FPS()

# Images ---------------------------------------------------------- #
asteroid_image = [pygame.image.load('data/asteroid_t1.png').convert_alpha(),
                  pygame.image.load('data/asteroid_t2.png').convert_alpha(),
                  pygame.image.load('data/asteroid_t3.png').convert_alpha()]
starship_image = [pygame.image.load('data/starship.png').convert_alpha(), 
                  pygame.image.load('data/starship_running.png').convert_alpha()]
laser_image =     pygame.image.load('data/laser.png').convert_alpha()
logo_image = pygame.transform.scale(pygame.image.load('data/logo.png').convert_alpha(), (1000, 300))
playbutton_image = [pygame.image.load('data/playbutton1.png').convert_alpha(), 
                    pygame.image.load('data/playbutton2.png').convert_alpha()]

# Sounds ---------------------------------------------------------- #

sounds = {
    'background' : pygame.mixer.Sound('data/sfx/background.wav'),
    'laser' : pygame.mixer.Sound('data/sfx/laser.wav'),
    'bump' : pygame.mixer.Sound('data/sfx/bump.wav')
}
sounds['background'].set_volume(0.1)
sounds['laser'].set_volume(0.01)
sounds['bump'].set_volume(0.05)

sounds['background'].play(-1)

# Menu preset ----------------------------------------------------- #
asteroids = []
for i in range(10):
    for j in range(3):
        asteroids.append(Asteroid(1, window_size, asteroid_image, random.randint(100, window_size[0] - 100), random.randint(100, window_size[1] - 100)))
    for j in range(4):
        asteroids.append(Asteroid(2, window_size, asteroid_image, random.randint(100, window_size[0] - 100), random.randint(100, window_size[1] - 100)))
    for j in range(3):
        asteroids.append(Asteroid(3, window_size, asteroid_image, random.randint(100, window_size[0] - 100), random.randint(100, window_size[1] - 100)))
    
last_time = time.time()
runningMenu = 1
cursor_on_btn = 0

# Menu loop ------------------------------------------------------- #
while runningMenu:
    current_time = time.time()
    dt = (current_time - last_time) * 60
    last_time = current_time
    
    mouseX, mouseY = pygame.mouse.get_pos() 
    clicked = 0

    screen.fill(BLACK)
    for ast in asteroids:
        ast.draw(screen)
     
    screen.blit(logo_image, (window_size[0] // 2 - logo_image.get_width() // 2, window_size[1] // 2 - logo_image.get_height() // 2 + math.sin(current_time * 5) * 10 - 25))
    screen.blit(playbutton_image[cursor_on_btn], (window_size[0] // 2 - playbutton_image[cursor_on_btn].get_width() // 2, window_size[1] // 2 - playbutton_image[cursor_on_btn].get_height() // 2 + 110))
    fps.draw(screen)
    fps.clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:            
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            clicked = 2

    if (mouseX - window_size[0] // 2) ** 2 + (mouseY - (window_size[1] // 2 + 110)) ** 2 < 75 ** 2:
        cursor_on_btn = 1
    else:
        cursor_on_btn = 0
            
    if clicked == 1 and cursor_on_btn or clicked == 2:
        runningMenu = 0
        sounds['laser'].play()

    for ast in asteroids:
        ast.dx = ast.mx * dt
        ast.dy = ast.my * dt
        ast.dangle = ast.mangle * dt        
        ast.update()

    pygame.display.update()        

# Game preset ----------------------------------------------------- #
starship = Starship(window_size, starship_image)
asteroids = []
lasers = []
last_time = start_time = time.time()
difficult = 1
runningGame = 1
tick = -1

# Game loop ------------------------------------------------------- #
while runningGame:      
    current_time = time.time()
    dt = (current_time - last_time) * 60    
    last_time = current_time  
    tick = (tick + 1) % (DIFFICULT_PERIOD + 1)        

    if tick % DIFFICULT_PERIOD == 0:
        difficult += 1    
        
    if tick % ASTEROID_SPAWN_PERIOD == 0:  
        for i in range(difficult):          
            asteroids.append(Asteroid(3, window_size, asteroid_image))
            asteroids.append(Asteroid(3, window_size, asteroid_image))
            asteroids.append(Asteroid(2, window_size, asteroid_image))
            asteroids.append(Asteroid(2, window_size, asteroid_image))
            asteroids.append(Asteroid(2, window_size, asteroid_image))
            asteroids.append(Asteroid(2, window_size, asteroid_image))                    
                         
    # Drawing ----------------------------------------------------- #    
    screen.fill(BLACK)
    for ast in asteroids:
        ast.draw(screen)
    for las in lasers:
        las.draw(screen)
    starship.draw(screen) 
    fps.draw(screen)    
    
    # Buttons ----------------------------------------------------- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:              
            pygame.quit()
            sys.exit()       
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
        if (tick % LASER_SPAWN_PERIOD == 0):            
            laser = Laser(starship.x, starship.y, starship.angle, laser_image)
            laser.mx = math.sin(math.radians(laser.angle)) * -1 * LASER_FLYING_SPEED
            laser.my = math.cos(math.radians(laser.angle)) * -1 * LASER_FLYING_SPEED  
            lasers.append(laser)
            sounds['laser'].play()                       
            
    # Update and collide ------------------------------------------ #  
    for ast in asteroids:
        ast.dx = ast.mx * dt
        ast.dy = ast.my * dt
        ast.dangle = ast.mangle * dt        
        ast.update()
        if starship.collide(ast.mask, ast.x, ast.y) != None:            
            starship.health -= ASTEROID_DAMAGE            
            if starship.health < STARSHIP_HP // 2:
                starship.healthbar_color = (255, 255, 0)        
            if starship.health < STARSHIP_HP // 4:
                starship.healthbar_color = (255, 0, 0)

            pygame.draw.rect(screen, starship.healthbar_color, pygame.Rect(starship.x - 20, starship.y - 20, starship.health / 100, 5))   
            sounds['bump'].play()     

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
    fps.clock.tick(60)  
