from pythoncraft.CharacterAnimation import *
from pythoncraft.Util import *

class Character(CharacterAnimation):
    def __init__(self,white):
        
        self.pos = vec((random.randint(0,200), random.randint(0,200)))
        self.white = white
        
        super().__init__() 

        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.exp = random.randint(0,1000)

        self.direction = ""

        
        chance = random.randint(0,999)
        self.name = None
        if type(self) is Agent:
            self.name = Text("Agent-"+str(chance), (255,0,0), 8, (0, 0))
        elif type(self) is Hacker:
            self.name = Text("Hacker-"+str(chance), (0,255,0), 8, (0, 0))
        elif type(self) is Peon:
            self.name = Text("Peon-"+str(chance), (255,255,255), 8, (0, 0))

        if self.white :
            white_characters.append(self)
            all_white_characters.add(self)
        else :
            black_characters.append(self)
            all_black_characters.add(self)
        characters.append(self)
        all_characters.add(self)
        all_sprites.add(self)

    def setDirection(self,direction):
        self.direction = direction
        
    def move(self):
        last_pos = self.pos
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

        if not self.collideGround():
            self.pos = last_pos
            self.rect.midbottom = self.pos

    def collideGround(self):
        collide = pygame.sprite.spritecollide(self, all_grounds, False, pygame.sprite.collide_mask)
        return collide
 
    def collide(self):
        collide = None
        if self.white :
            collide = pygame.sprite.spritecollide(self, all_white_characters, False, pygame.sprite.collide_mask)
        else :
            collide = pygame.sprite.spritecollide(self, all_black_characters, False, pygame.sprite.collide_mask)
    
        if self in collide:
            collide.remove(self)
        return collide
    
    def tryKill(self,character):
        if self.exp > character.exp :
            character.kill()


class Hacker(Character):
    def __init__(self,white):
        super().__init__(white)

class Agent(Character):
    def __init__(self,white):
        super().__init__(white)

class Peon(Character):
    def __init__(self,white):
        super().__init__(white)

     

