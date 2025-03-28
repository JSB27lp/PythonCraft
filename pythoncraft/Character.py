from pythoncraft.CharacterAnimation import *
from pythoncraft.Util import *
from pythoncraft.Tile import * 
from pythoncraft.Mineral import * 
from pythoncraft.Chest import * 
from pythoncraft.Player import * 

class Character(CharacterAnimation):
    def __init__(self,white,pos):
        
        self.pos = vec((random.randint(-100,100), random.randint(-100,100)))
        if pos != vec(0,0):
            self.pos = pos
        self.white = white
        
        super().__init__() 

        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.blue_minerals = 0
        self.pink_minerals = 0

        self.direction = ""

        
        chance = random.randint(0,999)
        self.name = None
        self.type = ""
        if type(self) is Hunter:
            self.name = Text("Hunter-"+str(chance), (0,255,0), 8, (0, 0))
            self.type ="Hunter"
        elif type(self) is Thief:
            self.name = Text("Thief-"+str(chance), (255,0,0), 8, (0, 0))
            self.type ="Thief"
        elif type(self) is Peon:
            self.name = Text("Peon-"+str(chance), (255,255,255), 8, (0, 0))
            self.type ="Peon"

        

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

        if self.collideWall():
            self.pos -= self.vel + 0.5 * self.acc
            self.rect.midbottom = self.pos

        if self.type == "Peon":
            self.collideMinerals()
            self.collideChest()
        
    def collideChest(self):
        collide = pygame.sprite.spritecollide(self, all_chests, False)
        if collide :
            if collide[0].white and self.white :
                collide[0].blue_minerals = self.blue_minerals
                collide[0].pink_minerals = self.pink_minerals

                self.blue_minerals = 0
                self.pink_minerals = 0

            if not collide[0].white and not self.white :
                collide[0].blue_minerals = self.blue_minerals
                collide[0].pink_minerals = self.pink_minerals
                
                self.blue_minerals = 0
                self.pink_minerals = 0

    def collideMinerals(self):
        collide = pygame.sprite.spritecollide(self, all_blue_minerals, True)
        if collide :
            self.blue_minerals += 1

        collide = pygame.sprite.spritecollide(self, all_pink_minerals, True)
        if collide :
            self.pink_minerals +=1

    def collideWall(self):
        collide = pygame.sprite.spritecollide(self, all_walls, False)
        return collide
 
    def collide(self):
        collide = None
        if self.white :
            collide = pygame.sprite.spritecollide(self, all_white_characters, False)
        else :
            collide = pygame.sprite.spritecollide(self, all_black_characters, False)
    
        if self in collide:
            collide.remove(self)
        return collide
    
    def tryKill(self,character):
        character.kill()


class Thief(Character):
    def __init__(self,white,pos=vec(0,0)):
        super().__init__(white,pos)

class Hunter(Character):
    def __init__(self,white,pos=vec(0,0)):
        super().__init__(white,pos)

class Peon(Character):
    def __init__(self,white,pos=vec(0,0)):
        super().__init__(white,pos)

     

