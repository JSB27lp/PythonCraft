from pythoncraft.head import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        
        self.surf = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.surf.fill((255,0,255))
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass
