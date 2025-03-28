import noise
from head import *
from Character.Character import *
from World.Tile import *


class World():
    def __init__(self):

        self.tiles = []

        self.characters = []

    def mapGeneration(self):
        #main
        character = Character(2,10,True,"Peon",True)
        self.characters.append(character)

        scale = 2
        octaves = 2
        lacunarity = 1.0
        persistence = 1.0

        for y in range(0,ROWS):
            row = []
            self.tiles.append(row)
            for x in range(0,COLS):

                value = noise.pnoise2(x/scale,y/scale,octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=ROWS,repeaty=COLS,base=0)
                if value <0 or x==0 or y==0 or x==COLS-1 or y==ROWS-1:
                    tile = Tile(x,y,"wall")
                else :
                    tile = Tile(x,y,"ground")

                    if not random.randint(0,30):
                        if len(self.characters)%2==0:
                            character = Character(x,y,True,"Peon",False)
                        else:
                            character = Character(x,y,False,"Peon",False)
                        self.characters.append(character)

                self.tiles[y].append(tile)

    def repopMinerals(self):
        pass

