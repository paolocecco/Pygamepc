import pygame




#Global Constants

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

map_list = [[0,0,0,0,1,1,0,0,0,0],
            [0,1,1,0,1,1,0,1,1,0],
            [0,1,1,0,1,1,0,1,1,0],
            [0,1,0,0,1,1,0,0,1,0],
            [0,0,0,1,1,1,1,0,0,0],
            [1,1,0,0,0,0,0,0,1,1],
            [1,0,0,1,1,0,1,0,0,1],
            [0,0,1,1,0,0,1,1,0,1],
            [0,1,1,1,0,1,1,1,0,1],
            [0,0,0,0,0,0,0,0,0,1]]

#Initialise PyGame

pygame.init()

#Blank Screen

size = (200,200)
screen = pygame.display.set_mode(size)
#Title of new window/screen
pygame.display.set_caption("Pacboy")


#Exit game flap set to false
done = False


##define class of tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_ref, y_ref):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref


#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.speed = 0
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 3
        self.rect.y = 3
        self.player_update_speed = (0,0) 
    
#pacman movement function
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player_update_speed = (-1,0)
            
        if keys[pygame.K_RIGHT]:
            self.player_update_speed = (1,0)

        if keys[pygame.K_DOWN]:
            self.player_update_speed = (0, 1)

        if keys[pygame.K_UP]:
            self.player_update_speed = (0, -1)

        if self.rect.x > 186:
            self.rect.x = 186
        elif self.rect.x < 0:
            self.rect.x = 0
        else:
            self.rect.x += self.player_update_speed[0]
        if self.rect.y > 186:
            self.rect.y = 186
        elif self.rect.y < 0:
            self.rect.y = 0
        else:
            self.rect.y += self.player_update_speed[1]
            player_hit_list = pygame.sprite.spritecollide(Player, map_list, False)
        for foo in player_hit_list:
            pacman.player_speed_update(0,0)
            pacman.rect.x = pacman_old_x
            pacman.rect.y = pacman_old_y
            pacman_old_x = pacman.rect.x
            pacman_old_y = pacman.rect.y



#create lists
all_sprites_list = pygame.sprite.Group()


wall_list = pygame.sprite.Group()

#create map
for y in range(10):
    for x in range(10):
        if map_list[y][x] == 1:
            my_wall = Tile(BLUE, 20, 20, x*20, y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)


pacman = Player(RED, 14, 14)
all_sprites_list.add(pacman)

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
    

    all_sprites_list.update()
    
    #screen background is BLACK
    screen.fill (BLACK)
    
    all_sprites_list.draw(screen)
    #draw here

    #flip display to reveal new postion of objects (refreshes screen)
    pygame.display.flip()
    #clock ticks over
    clock.tick(60)

#endwhile - End of game loop

pygame.quit