from pythoncraft.head import *
from pythoncraft.Util import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.surf = pygame.surface.Surface((10,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect() 

    def getPosCursor(self):
        mousex, mousey = pygame.mouse.get_pos()
        ratio = W_SCREEN/W_SURF     
        x = mousex/ratio
        y = mousey/ratio

        return vec(x,y)

    def play(self):

        vec_tmp = self.getPosCursor()
        self.rect.center = vec_tmp
        display_surf.blit(self.surf, self.rect)