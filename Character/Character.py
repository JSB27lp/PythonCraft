from Character.CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self,x,y,white,type,main):
    
        self.main = main

        self.x = x
        self.y = y
        self.cpt_frames = 0
        self.direction = ""

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

    def move(self,tiles):
        self.changeDirection()
                
        if self.direction == "left":
                self.x -= VELOCITY

        if self.direction == "right":
            self.x += VELOCITY

        if self.direction == "up":
            self.y -= VELOCITY

        if self.direction == "down":
            self.y += VELOCITY

        self.rect.midbottom = (self.x*TILE_SIZE+OFFSET_X,self.y*TILE_SIZE+OFFSET_Y)

        self.animate()

    def changeDirection(self):
            self.cpt_frames+=1
            if self.cpt_frames>8:
                if not self.main:
                    direction = random.choice(["up", "down", "right", "left",""])
                    self.direction = direction
                    self.cpt_frames = 0

    def testMinerals(self):
        pass

    def testChests(self):
        pass
