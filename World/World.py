import noise
from head import *
from Character.Peon import *
from Character.Hunter import *
from Character.Thief import *
from World.Tile import *


class World():
    def __init__(self):

        self.tiles = []
        for y in range(0,ROWS):
            row = []
            self.tiles.append(row)

        self.characters = []

        self.grounds = []
        self.minerals = []

    def genWorld(self):
        scale = 2
        octaves = 2
        lacunarity = 1.0
        persistence = 1.0

        for y in range(0,ROWS):
            for x in range(0,COLS):

                value = noise.pnoise2(x/scale,y/scale,octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=ROWS,repeaty=COLS,base=0)
                if value <0 or x==0 or y==0 or x==COLS-1 or y==ROWS-1:
                    tile = Tile(x,y,"wall")
                else :
                    tile = Tile(x,y,"ground")
                    self.grounds.append(tile)

                    if not random.randint(0,20) :
                        tile.mineral = Mineral(x,y)
                        self.minerals.append(tile.mineral)

                self.tiles[y].append(tile)

    def genChests(self):
        
        chance1 = random.randint(0,len(self.grounds))
        if self.grounds[chance1].chest == None:
            chest = Chest(self.grounds[chance1].x,self.grounds[chance1].y,True)
            self.grounds[chance1].chest = chest

        chance2 = random.randint(0,len(self.grounds))
        if self.grounds[chance2].chest == None:
            chest = Chest(self.grounds[chance2].x,self.grounds[chance2].y,False)
            self.grounds[chance2].chest = chest

    def genCharacters(self):
        
        #main
        chance = random.randint(0,len(self.grounds))
        character = Thief(self.grounds[chance].x,self.grounds[chance].y,False,"Thief",True)
        self.characters.append(character)

        for i in range(0,4):
            chance = random.randint(0,len(self.grounds))
            character = Peon(self.grounds[chance].x,self.grounds[chance].y,False,"Peon",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Peon(self.grounds[chance].x,self.grounds[chance].y,True,"Peon",False)
            self.characters.append(character)

        for i in range(0,2):
            chance = random.randint(0,len(self.grounds))
            character = Hunter(self.grounds[chance].x,self.grounds[chance].y,False,"Hunter",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Hunter(self.grounds[chance].x,self.grounds[chance].y,True,"Hunter",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Thief(self.grounds[chance].x,self.grounds[chance].y,False,"Thief",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Thief(self.grounds[chance].x,self.grounds[chance].y,True,"Thief",False)
            self.characters.append(character)

    def repopMinerals(self):
        if len(self.minerals)<25:
            chance = random.randint(0,len(self.grounds))
            if self.grounds[chance].mineral == None:
                mineral = Mineral(self.grounds[chance].x,self.grounds[chance].y)
                self.minerals.append(mineral)
                self.grounds[chance].mineral = mineral

