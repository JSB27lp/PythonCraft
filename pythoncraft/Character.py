from pythoncraft.CharacterAnimation import *
from pythoncraft.Util import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 

        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.direction = ""

        chance = random.randint(0,999)
        self.name = Text("Smith-"+str(chance), (255,255,255), 8, (0, 0))

    def setName(self, name):
        self.name = Text(name, (255,255,255), 8, (0, 0))
        
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

     

