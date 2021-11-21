import pygame
import math
import random

from pygame.draw import rect

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
    def __init__(self, color, width, height, speed):
        #CALL the SPRITE CONSTRUCTOR
        super().__init__()
        #set speed of sprite
        self.speed = speed
        #create SPRITE and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the SPRITE
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,640)
        self.rect.y = random.randrange(0,480)
    #end procedure
    def update(self):
        if self.rect.y >480:
            self.rect.y = -5
            self.rect.x = random.randrange(0,640)
        else:
            self.rect.y = self.rect.y + self.speed
    #end procedure
#end class


#Exit gae flap set to false
done = False

#create a list of the snow blocks
snow_group = pygame.sprite.Group()

#create a list of all sprites
all_sprites_group = pygame.sprite.Group()

#Manages how fast screen refreshes
clock = pygame.time.Clock()


#create the snowflakes
number_of_flakes = 50 #50 snowflakes
for x in range (number_of_flakes):
    my_snow = Snow(WHITE, 5, 5, 1) #snowflakes made white with dimensions 5 by 5
    snow_group.add (my_snow) #adds the new snowflake to the group of snowflakes
    all_sprites_group.add (my_snow) #adds this snowflake to group of sprites

#next



### GAME LOOP

while not done:

    #user input and controls

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        #endif
    #next event
    
    #Game logic goes after this comment
    all_sprites_group.update()

    #screen background is BLACK
    screen.fill (BLACK)
    
    #draw here
    all_sprites_group.draw (screen)
    #flip display to reveal new postion of objects (refreshes screen)
    pygame.display.flip()
    #clock ticks over
    clock.tick(60)

#endwhile - End of game loop

pygame.quit