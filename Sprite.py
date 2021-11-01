import pygame
import math
import random

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
pygame.display.set_caption("Snow")

##DEFINE the class SNOW which is a SPRITE
class Snow(pygame.sprite.Sprite):
    #define the CONSTRUCTOR for SNOW
    def __init__(self, color, width, height):
        #CALL the SPRITE CONSTRUCTOR
        super().__init__()
        #create SPRITE and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the SPRITE
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(0,400)
    #end procedure
#end class


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