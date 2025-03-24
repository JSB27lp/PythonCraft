from pythoncraft.CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 
   
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.jumping = False

        self.dir = ""
        
    def move(self):
        self.acc = vec(0,0)
                
        if self.dir == "left":
            self.acc.x = -ACC
            self.last_dir = "left"

        if self.dir == "right":
            self.acc.x = ACC
            self.last_dir = "right"

        if self.dir == "up":
            self.acc.y = -ACC
            self.last_dir = "up"

        if self.dir == "down":
            self.acc.y = ACC
            self.last_dir = "down"

        self.animate()
                 
        self.acc += self.vel * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        self.rect.midbottom = self.pos
 
    def checkCollisions(self):
        pass
        '''if self.vel.y > 0:    
            collide = pygame.sprite.spritecollide(self, platforms, False, pygame.sprite.collide_mask)
            if collide:
                pass'''

