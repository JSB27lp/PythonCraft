from CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 
   
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.jumping = False
        
    def move(self):
        self.acc = vec(0,0)
                
        if textinput.value == "p1.left()":
            self.acc.x = -ACC
            self.last_dir = "left"

        if textinput.value == "p1.right()":
            self.acc.x = ACC
            self.last_dir = "right"

        if textinput.value == "p1.up()":
            self.acc.y = -ACC
            self.last_dir = "up"

        if textinput.value == "p1.down()":
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

