import random


Done = False

num_players = int(input("how many players do you want, 1-5"))

s_l_start = [93, 86, 83, 80, 67, 57, 44, 35, 22, 18,   5, 15, 36, 48, 60, 75] #16 items
s_l_end =   [33, 70, 65, 61, 20, 32, 28, 18, 10, 2,    12, 38, 42, 85, 71, 90]
names_list = [1, 2, 3, 4, 5] #max of 5 players
players = []


###Classes
     



#player class
class Player():
    def __init__(self, n):
        self.playerpos = 0
        self.playerName = n

    def set_playerpos(self):
        return (self.playerpos)

    def get_name(self):
        return (self.)


    #roll dice and update position
    def rolldice(self):
        return (random.randint(1,6))


    #update position of player
    def update(self, p):
        self.playerpos = p
 

    

#initialise player list
for count in range(1, num_players):
    p = Player
    p.playerName = names_list[count-1]
    players.append(p.playerName)



#snakes and ladders class
class SnakesLadder():
    def __init__(self):
        self.obstart = s_l_start
        self.obsend = s_l_end




class Board():
    def __init__(self):
        self.size = 100
        self.player_list = []
        self.obs_list = []
        self.dice = Player.rolldice
        for n in num_players:
            Player(names_list(n))
            self.player_list.append







        


#game loop
while Done == False:
    if str(input("input exit to exit game, enter anything else to play again")) == "exit" :
        Done == True
    else:
        
                






###
       self.playerpos = self.rolldice()
        if self.playerpos == s_l_start:
            self.playerpos == s_l_end
        print("Player", self.playerName, ":", self.playerpos)
        if self.playerpos > 99:
            print("Player", self.playerName, "wins")        
            Done = True