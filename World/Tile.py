from head import *
from Object.Mineral import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type):
        super().__init__()
        
        self.type = type

        if self.type == "ground":
            self.surf = ground_cave_img
            
            #gen minerals
            if not random.randint(0,5) :
                self.mineral = Mineral(x,y)
        else :
            self.surf = wall_cave_img

        self.rect = self.surf.get_rect(center = (x*TILE_SIZE+OFFSET_X,y*TILE_SIZE+OFFSET_Y))

        all_tiles.add(self)





    def display(self):
        display_surf.blit(self.surf, self.rect)
