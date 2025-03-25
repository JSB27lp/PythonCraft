from pythoncraft.CharacterAnimation import *
from pythoncraft.Util import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 

        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.exp = 0

        self.direction = ""

        
        chance = random.randint(0,999)
        self.name = None
        if type(self) is Agent:
            self.name = Text("Agent-"+str(chance), (255,255,255), 8, (0, 0))
        if type(self) is Hacker:
            self.name = Text("Hacker-"+str(chance), (0,255,0), 8, (0, 0))

    def setDirection(self,direction):
        self.direction = direction
        
    def move(self):
        self.acc = vec(0,0)
                
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
             
        self.rect.midbottom = self.pos
 
    def checkCollisions(self):
        collide = pygame.sprite.spritecollide(self, tiles_group, False, pygame.sprite.collide_mask)
        if collide:
            print("collision")

class Hacker(Character):
    def __init__(self):
        super().__init__()

class Ia(Character):
    def __init__(self):
        super().__init__()

class Ceo(Character):
    def __init__(self):
        super().__init__()

class Agent(Character):
    def __init__(self):
        super().__init__()

class Politician(Character):
    def __init__(self):
        super().__init__()

class Peon(Character):
    def __init__(self):
        super().__init__()

     

