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
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT] or pressed_keys[K_q] :
            self.acc.x = -ACC
            self.last_dir = -1
        if pressed_keys[K_RIGHT] or pressed_keys[K_d] :
            self.acc.x = ACC
            self.last_dir = 1
        if pressed_keys[K_UP] or pressed_keys[K_z] :
            self.acc.y = -ACC
            self.last_dir = -1
        if pressed_keys[K_DOWN] or pressed_keys[K_s] :
            self.acc.y = ACC
            self.last_dir = 1

        self.animate()
                 
        self.acc += self.vel * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        self.rect.midbottom = self.pos
 
    def checkCollisions(self):
        if self.vel.y > 0:    
            collide = pygame.sprite.spritecollide(self, platforms, False, pygame.sprite.collide_mask)
            if collide:
                pass

