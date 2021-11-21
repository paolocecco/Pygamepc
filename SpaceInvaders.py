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
pygame.display.set_caption("Space Invaders")

##DEFINE the class SNOW which is a SPRITE
class Invaders(pygame.sprite.Sprite):
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
        self.rect.y = random.randrange(0,100)
    #end procedure

    def update(self):
        if self.rect.y >480:
            self.rect.y = -5
            self.rect.x = random.randrange(0,640)
        else:
            self.rect.y = self.rect.y + self.speed
    #end procedure


    
#end class


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.speed = 0
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 460


    def update(self):
        if self.rect.x > 579:
            self.rect.x = 580
        elif self.rect.x < 1:
            self.rect.x = 0
        else:
            self.rect.x = self.rect.x + self.speed


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.speed=-5
                elif event.key == pygame.K_RIGHT:
                    self.speed=5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.speed = 0
        

done = False

#create a list of the snow blocks
invaders_group = pygame.sprite.Group()

#create list of player(s)
players_group = pygame.sprite.Group()

#create a list of all sprites
all_sprites_group = pygame.sprite.Group()

clock = pygame.time.Clock()


#create the enemies
number_of_enemies = random.randrange(10,20)
for x in range (number_of_enemies):
    my_invader = Invaders(BLUE, 20, 8, 1) #enemies made white with dimensions 5 by 5
    invaders_group.add (my_invader) #adds the new enemy to the group of enemies
    all_sprites_group.add (my_invader) #adds this enemy to group of sprites

#next

my_player = Player(WHITE, 60, 10)
players_group.add(my_player)
all_sprites_group.add (my_player)


### GAME LOOP

while not done:

    #user input and controls

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done =  True
    
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