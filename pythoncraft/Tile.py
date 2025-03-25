from pythoncraft.head import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        
        self.surf = tilesetSheet1
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass
