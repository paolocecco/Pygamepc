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
pygame.display.set_caption("My Window")
#Exit gae flap set to false
done = False
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

    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (40,100),40,0)
    #flip display to reveal new postion of objects (refreshes screen)
    pygame.display.flip()
    #clock ticks over
    clock.tick(60)

#endwhile - End of game loop

pygame.quit