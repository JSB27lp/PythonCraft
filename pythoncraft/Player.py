from pythoncraft.head import *
from pythoncraft.Util import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

    def play(self):
        tmp = pygame.surface.Surface((10,10))
        tmp.fill((255,255,255))

        vec_tmp = getPosCursor()
        display_surf.blit(tmp, (vec_tmp.x, vec_tmp.y))