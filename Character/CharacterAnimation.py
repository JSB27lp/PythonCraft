from head import *
from Util.Text import *

class CharacterAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.index_frame_run = 0 #that keeps track on the current index of the image list.
        self.current_frame_run = 0 #that keeps track on the current time or current frame since last the index switched. 

        all_characters.add(self)
            
        self.surf = self.surf = run_sheets[self.white].subsurface((run_sheet_white.get_width()/8*self.index_frame_run,run_sheet_white.get_height()/3*0,run_sheet_white.get_width()/8,run_sheet_white.get_height()/3))

        self.surf_square = pygame.surface.Surface((idle_sheet_white.get_width()/8- 32,idle_sheet_white.get_height()/3- 64)) #
        self.surf_square.fill((255,0,255))
        
        self.rect = self.surf_square.get_rect(midbottom = (0,0))

    def animate(self):
        self.runAnimation()

    def runAnimation(self):
        if self.direction == "right" :
            self.surf = run_sheets[self.white].subsurface((run_sheet_white.get_width()/8*self.index_frame_run,run_sheet_white.get_height()/3*0,run_sheet_white.get_width()/8,run_sheet_white.get_height()/3))
        elif self.direction == "left" :
            self.surf = run_sheets[self.white].subsurface((run_sheet_white.get_width()/8*self.index_frame_run,run_sheet_white.get_height()/3*0,run_sheet_white.get_width()/8,run_sheet_white.get_height()/3))
            self.surf = pygame.transform.flip(self.surf, True, False)
        elif self.direction == "up" :
            self.surf = run_sheets[self.white].subsurface((run_sheet_white.get_width()/8*self.index_frame_run,run_sheet_white.get_height()/3*2,run_sheet_white.get_width()/8,run_sheet_white.get_height()/3))
        elif self.direction == "down" :
            self.surf = run_sheets[self.white].subsurface((run_sheet_white.get_width()/8*self.index_frame_run,run_sheet_white.get_height()/3*1,run_sheet_white.get_width()/8,run_sheet_white.get_height()/3))

        self.current_frame_run += 1
        if self.current_frame_run >= NB_FRAMES_SWITCH:
            self.current_frame_run = 0
            self.index_frame_run += 1
            if self.index_frame_run >= 8 :
                self.index_frame_run = 0  

    def display(self):

        #DEBUG
        #display_surf.blit(self.surf_square, (self.rect.x - camera.x -36, self.rect.y - camera.y -32))


        display_surf.blit(self.surf, (self.rect.x -36, self.rect.y -32))
     

     
        #info display personnage
        display_surf.blit(self.name.surf, (self.rect.x -15, self.rect.y -10))   

        exp_txt = Text(str(self.blue_minerals), (0,255,255), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x  -15, self.rect.y -15))   

        exp_txt = Text(str(self.pink_minerals), (255,20,147), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x -15, self.rect.y -20))


