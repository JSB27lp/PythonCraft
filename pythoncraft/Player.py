from pythoncraft.head import *
from pythoncraft.Util import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.surf = pygame.surface.Surface((10,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = getPosCursor()) 

    def play(self):

        vec_tmp = getPosCursor()
        display_surf.blit(self.surf, (vec_tmp.x, vec_tmp.y))