from pythoncraft.head import *
from pythoncraft.Util import *
from pythoncraft.Character import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.surf = pygame.surface.Surface((10,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = self.getPosCursor()) 

    def getPosCursor(self):
        mousex, mousey = pygame.mouse.get_pos()
        ratio = W_SCREEN/W_SURF     
        x = mousex/ratio
        y = mousey/ratio

        return vec(x,y)
    
    def updateRect(self):
        vec_tmp = self.getPosCursor()
        self.rect.center = vec_tmp

    def play(self):
        self.updateRect()

        if self.collideCharacters() :
            print("collision")

        #display_surf.blit(self.surf, self.rect)

    def collideCharacters(self):
        collide = pygame.sprite.spritecollide(self, all_characters, False)
        return collide

    