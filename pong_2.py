import pygame

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
pygame.display.set_caption("Pong")
#Exit gae flap set to false
done = False
#Manages how fast screen refreshes
clock = pygame.time.Clock()

ball_width = 20
x_val = 150
y_val = 200
x_dir = 1
y_dir = 1
padd_len = 15
padd_w = 60
x_padd = 0
y_padd = 200



### GAME LOOP

while not done:

    #user input and controls

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        #endif
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_padd < 1:
                    y_padd = 0
                else:
                    y_padd = y_padd - 20
            elif event.key == pygame.K_DOWN:
                if y_padd > 419:
                    y_padd = 420
                else:
                    y_padd = y_padd + 20
    #next event
    
    #Game logic goes after this comment
    #screen background is BLACK
    screen.fill (BLACK)
    
    #draw here

    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_len, padd_w))
    #flip display to reveal new postion of objects (refreshes screen)
    pygame.display.flip()
    #clock ticks over
    clock.tick(60)
    if y_val > 460:
        y_dir = y_dir * -1
    #endif
    if y_val < 0:
        y_dir =  y_dir * -1
    #endif
    if x_val > 620:
        x_dir = x_dir * -1
    #endif
    if x_val < 0:
        x_dir = x_dir * -1
    #endif
    x_val += x_dir # x_val = x_val + x_dir
    y_val += y_dir # y_val = y_val + y_dir



#endwhile - End of game loop

pygame.quit