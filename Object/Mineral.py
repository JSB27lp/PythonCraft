from head import *

class Mineral(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.type = random.choice(["blue", "pink"])
        if self.type == "blue":
            self.surf = mineral_sheet.subsurface((0,0,mineral_sheet.get_width()/4,mineral_sheet.get_height()/2))
        else : 
            self.surf = mineral_sheet.subsurface((0,mineral_sheet.get_height()/2,mineral_sheet.get_width()/4,mineral_sheet.get_height()/2))

        self.rect = self.surf.get_rect(center = (x*TILE_SIZE+OFFSET_X,y*TILE_SIZE+OFFSET_Y))

        all_minerals.add(self)

    def display(self):
        display_surf.blit(self.surf, self.rect)