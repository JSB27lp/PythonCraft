from pythoncraft.head import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf):
        super().__init__()
        
        self.surf = surf
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center = pos)
        print(pos)

    def move(self):
        pass

    def display(self,camera):
        display_surf.blit(self.surf, (self.rect.x - camera.x, self.rect.y - camera.y))

