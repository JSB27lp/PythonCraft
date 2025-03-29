from pythoncraft.head import *
from pythoncraft.Util import *

class Chest(pygame.sprite.Sprite):
    def __init__(self,pos,white):
        super().__init__()

        self.white = white

        self.surf = chest_img

        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center = pos)

        all_sprites.add(self)
        all_chests.add(self)

        self.blue_minerals = 0
        self.pink_minerals = 0

    def move(self):
        pass

    def display(self,camera):
        display_surf.blit(self.surf, (self.rect.x - camera.x, self.rect.y - camera.y))

        exp_txt = Text(str(self.blue_minerals), (0,255,255), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x - camera.x +5 , self.rect.y - camera.y -5))   

        exp_txt = Text(str(self.pink_minerals), (255,20,147), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x - camera.x +5, self.rect.y - camera.y -10 ))