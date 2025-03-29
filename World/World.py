import noise
from head import *
from Character.Character import *
from World.Tile import *


class World():
    def __init__(self):

        self.tiles = []
        for y in range(0,ROWS):
            row = []
            self.tiles.append(row)

        self.characters = []

        #pour faciliter la gestion interne de world
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

                    if not random.randint(0,10) :
                        tile.mineral = Mineral(x,y)
                        self.minerals.append(tile.mineral)

                self.tiles[y].append(tile)

    def genCharacters(self):
        
        #main
        character = Character(2,10,True,"Peon",True)
        self.characters.append(character)

        for i in range(0,5):
            chance = random.randint(0,len(self.grounds))
            character = Character(self.grounds[chance].x,self.grounds[chance].y,False,"Peon",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Character(self.grounds[chance].x,self.grounds[chance].y,True,"Peon",False)
            self.characters.append(character)

        for i in range(0,2):
            chance = random.randint(0,len(self.grounds))
            character = Character(self.grounds[chance].x,self.grounds[chance].y,False,"Hunter",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Character(self.grounds[chance].x,self.grounds[chance].y,True,"Hunter",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Character(self.grounds[chance].x,self.grounds[chance].y,False,"Thief",False)
            self.characters.append(character)

            chance = random.randint(0,len(self.grounds))
            character = Character(self.grounds[chance].x,self.grounds[chance].y,True,"Thief",False)
            self.characters.append(character)

    def repopMinerals(self):
        if len(self.minerals)<25:
            chance = random.randint(0,len(self.grounds))
            mineral = Mineral(self.grounds[chance].x,self.grounds[chance].y)
            self.minerals.append(mineral)

