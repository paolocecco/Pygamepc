import random


Done = False

num_players = int(input("how many players do you want, 1-5"))

s_l_start = [93, 86, 83, 80, 67, 57, 44, 35, 22, 18,   5, 15, 36, 48, 60, 75] #16 items
s_l_end =   [33, 70, 65, 61, 20, 32, 28, 18, 10, 2,    12, 38, 42, 85, 71, 90]
names_list = [1, 2, 3, 4, 5]
snakesladder_list = []
players = []


###Classes

class Board():
    def __init__(self):
        self.size = 100
        
        
    #player class
    class Player():
        def __init__(self, playerName):
            self.playerpos = 0
            self.playerName = self.playerName


        #roll dice and update position
        def rolldice(self):
            self.playerpos = self.playerpos + (random.randint(1,6))


        def update(self):
            self.playerpos = self.rolldice(self.position)
            print("Player", self.playerName, ":", self.playerpos)
            if self.playerpos > 99:
                print("Player", self.playerName, "wins")        
                Done = True


    for count in range(1, num_players):
        p = Player
        p.playerName = names_list[count-1]
        players.append(p(count))


    #snakes and ladders class
    class SnakesLadder():
        def __init__(self):
            self.obstart = self.obstart
            self.obsend = self.obsend

    
    for count in range(1, 16):
        s = SnakesLadder()
        s.obstart = s_l_start[count]
        s.obsend = s_l_end[count]
        snakesladder_list.append(s)
    



        




while Done == False:
    if str(input("input exit to exit game, enter anything else to play again")) == "exit":
        Done == True
    else:
        print(snakesladder_list)
