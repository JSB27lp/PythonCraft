from pythoncraft.head import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf):
        super().__init__()
        
        self.surf = surf
        self.rect = self.surf.get_rect(center = pos)

        all_sprites.add(self)
        all_tiles.add(self)

    def move(self):
        pass

    def display(self,camera):
        display_surf.blit(self.surf, (self.rect.x - camera.x, self.rect.y - camera.y))

