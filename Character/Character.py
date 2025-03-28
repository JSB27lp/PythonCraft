from Character.CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self,x,y,white,type,main):
        super().__init__(x,y)

        self.main = main

        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
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

    def move(self):
        self.acc = vec(0,0)

        self.chooseDirection()
                
        if self.direction == "left":
            self.acc.x = -ACC
            self.last_dir = "left"

        if self.direction == "right":
            self.acc.x = ACC
            self.last_dir = "right"

        if self.direction == "up":
            self.acc.y = -ACC
            self.last_dir = "up"

        if self.direction == "down":
            self.acc.y = ACC
            self.last_dir = "down"

        self.animate()
                 
        self.acc += self.vel * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        self.rect.midbottom = vec(self.pos.x*TILE_SIZE+OFFSET_X,self.pos.y*TILE_SIZE+OFFSET_Y)

    def chooseDirection(self):
        self.cpt_frames += 1
        if self.cpt_frames > NB_FRAMES_SWITCH :
            if not self.main:
                direction = random.choice(["up", "down", "right", "left"])
                if not random.randint(0,3) : 
                    self.setDirection(direction)

        self.cpt_frames = 0

    def testCollision(self):
        pass
