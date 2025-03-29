from head import *
from Util.Text import *

class Chest(pygame.sprite.Sprite):
    def __init__(self,x,y,white):
        super().__init__()

        self.white = white

        self.surf = chest_img
        self.rect = self.surf.get_rect(center = (x*TILE_SIZE+OFFSET_X,y*TILE_SIZE+OFFSET_Y))

        all_chests.add(self)

        self.blue_minerals = 0
        self.pink_minerals = 0

    def display(self):
        display_surf.blit(self.surf, (self.rect.x, self.rect.y -2))

        exp_txt = Text(str(self.blue_minerals), (0,255,255), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x +5 , self.rect.y -5))   

        exp_txt = Text(str(self.pink_minerals), (255,20,147), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x +5, self.rect.y -10 ))