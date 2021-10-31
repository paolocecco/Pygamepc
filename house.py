import pygame
import math

#Global Constants

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#Initialise PyGame

pygame.init()

#Blank Screen

size = (640,480)
screen = pygame.display.set_mode(size)
#Title of new window/screen
pygame.display.set_caption("House")
#Exit gae flap set to false
done = False
sun_x = 40
sun_y = 100
house_x = 220
house_y =165
house_w = 200
house_h = 150
gap = 30
win_w = 30
#Manages how fast screen refreshes
clock = pygame.time.Clock()


### GAME LOOP

while not done:

    #user input and controls

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        #endif
    #next event
    

    #Game logic goes after this comment
    #screen background is BLACK
    screen.fill (BLACK)
    
    #draw here

    pygame.draw.rect(screen, BLUE, (house_x, house_y, house_w, house_h))
    pygame.draw.rect(screen, WHITE, (house_x + gap, house_y + gap, win_w, win_w))
    pygame.draw.rect(screen, WHITE, (house_x + house_w - gap - win_w, house_y + gap, win_w, win_w))
    pygame.draw.rect(screen, WHITE, (house_x + gap, house_y + house_h - gap - win_w, win_w, win_w))
    pygame.draw.rect(screen, WHITE, (house_x + house_w - gap - win_w, house_y + house_h - gap - win_w, win_w, win_w))
    pygame.draw.rect(screen, WHITE, (house_x + (house_w - win_w)/2, house_y + house_h - 2*win_w, win_w, 2*win_w))

    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y), 40, 0)
    
    sun_x += 5
    if sun_x > size[0]:
        sun_x = 0

    w = size[0]/2
    x = sun_x - w
    sun_y = 200 - math.sqrt(w*w - x*x) / 2

    #flip display to reveal new postion of objects (refreshes screen)
    pygame.display.flip()
    #clock ticks over
    clock.tick(20)

#endwhile - End of game loop

pygame.quit