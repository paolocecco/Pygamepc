import random


Done = False

num_players = int(input("how many players do you want"))
###Classes

class Board():
    def __init__(self):
        self.size = 100
        
    #player class
    class Player():
        def __init__(self, playerName):
            self.playerpos = 0
            self.playerName = self.playerName

    players = []
    for count in range(1, num_players):
        players.append(Player(count))

    #snakes and ladders clas
    class S_L():
        def __init__(self, obsStart, obsEnd):
            self.obstart = self.obstart
            self.obsend = self.obsend
            
        def move_player(self):


    snakesladder = []
    for count in range(1, 16):
        snakesladder.append(S_L(random.randint(2,99)),(random.randint(2,99)))

        




while Done == False:
    if str(input("input exit to exit game, enter anything else to play again")) == "exit":
        Done == True

