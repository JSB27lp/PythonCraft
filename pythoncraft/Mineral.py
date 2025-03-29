from pythoncraft.head import *

class Mineral(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.type = random.choice(["blue", "pink"])
        if self.type == "blue":
            self.surf = mineralSheet.subsurface((0,0,mineralSheet.get_width()/4,mineralSheet.get_height()/2))
        else : 
            self.surf = mineralSheet.subsurface((0,mineralSheet.get_height()/2,mineralSheet.get_width()/4,mineralSheet.get_height()/2))

        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center = pos)

        
        all_sprites.add(self)
        if self.type == "blue":
            all_blue_minerals.add(self)
        else :
            all_pink_minerals.add(self)

        

    def move(self):
        pass

    def display(self,camera):
        display_surf.blit(self.surf, (self.rect.x - camera.x, self.rect.y - camera.y))