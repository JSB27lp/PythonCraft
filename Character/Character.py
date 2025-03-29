from Character.CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self,x,y,white,type,main):
    
        self.main = main

        self.x = x
        self.y = y
        self.cpt_frames = 0
        self.direction = ""

        self.tile=None

        self.white = white

        self.blue_minerals = 0
        self.pink_minerals = 0

        self.type = type
        
        self.name = None
        chance = random.randint(0,999)
        if self.type == "Hunter":
            if self.main:
                self.name = Text("Hunter-"+str(chance), (0,0,255), 8, (0, 0))
            else:
                self.name = Text("Hunter-"+str(chance), (0,255,0), 8, (0, 0))
        elif self.type == "Thief":
            if self.main:
                self.name = Text("Thief-"+str(chance), (0,0,255), 8, (0, 0))
            else :
                self.name = Text("Thief-"+str(chance), (255,0,0), 8, (0, 0))
        elif self.type == "Peon":
            if self.main:
                self.name = Text("Peon-"+str(chance), (0,0,255), 8, (0, 0))
            else:
                self.name = Text("Peon-"+str(chance), (255,255,255), 8, (0, 0))

        super().__init__()

    def updateTile(self,tiles):
        a = round(self.x)
        b = round(self.y)
        self.tile = tiles[b][a]

    def newPosition(self,x_gain,y_gain):
        velo = 0.1

        self.x = self.x + (velo*x_gain) 
        self.y = self.y + (velo*y_gain) 

    def move(self,world):
        if self.direction == "left":
            self.newPosition(-1,0)
            self.updateTile(world.tiles)
            if self.tile.type=="wall":
                self.newPosition(1,0)

        if self.direction == "right":
            self.newPosition(1,0)
            self.updateTile(world.tiles)
            if self.tile.type=="wall":
                self.newPosition(-1,0)

        if self.direction == "up":
            self.newPosition(0,-1)
            self.updateTile(world.tiles)
            if self.tile.type=="wall":
                self.newPosition(0,1)

        if self.direction == "down":
            self.newPosition(0,1)
            self.updateTile(world.tiles)
            if self.tile.type=="wall":
                self.newPosition(0,-1)

        self.rect.midbottom = (self.x*TILE_SIZE+OFFSET_X,self.y*TILE_SIZE+OFFSET_Y)

        self.animate()

    def pathFinding(self):
            self.cpt_frames+=1
            if self.cpt_frames>8:
                if not self.main:
                    direction = random.choice(["up", "down", "right", "left",""])
                    self.direction = direction
                    self.cpt_frames = 0

    def testChests(self):
        if self.tile.chest != None:
            if self.white and self.tile.chest.white:
                self.tile.chest.blue_minerals += self.blue_minerals
                self.tile.chest.pink_minerals += self.pink_minerals

                self.blue_minerals = 0
                self.pink_minerals = 0
            
            if not self.white and not self.tile.chest.white:
                self.tile.chest.blue_minerals += self.blue_minerals
                self.tile.chest.pink_minerals += self.pink_minerals

                self.blue_minerals = 0
                self.pink_minerals = 0

    def action(self):
        pass
