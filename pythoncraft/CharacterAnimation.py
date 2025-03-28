from pythoncraft.head import *
from pythoncraft.Util import *

class CharacterAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
            
        self.surf = idle_sheet.subsurface((0,0,idle_sheet.get_width()/8,idle_sheet.get_height()/3))

        self.surf_square = pygame.surface.Surface((idle_sheet.get_width()/8- 32,idle_sheet.get_height()/3- 64)) #
        self.surf_square.fill((255,0,255))
        
        self.rect = self.surf_square.get_rect(midbottom = self.pos)

        self.last_dir = "right"

        self.index_frame_idle = 0 #that keeps track on the current index of the image list.
        self.current_frame_idle = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_run = 0 #that keeps track on the current index of the image list.
        self.current_frame_run = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_walk = 0 #that keeps track on the current index of the image list.
        self.current_frame_walk = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_hurt = 0 #that keeps track on the current index of the image list.
        self.current_frame_hurt = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_death = 0 #that keeps track on the current index of the image list.
        self.current_frame_death = 0 #that keeps track on the current time or current frame since last the index switched. 

    def animate(self):
        if self.acc.x != 0:
            self.runAnimation()
        else :
            self.idleAnimation()

    def runAnimation(self):
        if self.last_dir == "right" :
            self.surf = run_sheets[self.white].subsurface((run_sheet.get_width()/8*self.index_frame_run,run_sheet.get_height()/3*0,run_sheet.get_width()/8,run_sheet.get_height()/3))
        elif self.last_dir == "left" :
            self.surf = run_sheets[self.white].subsurface((run_sheet.get_width()/8*self.index_frame_run,run_sheet.get_height()/3*0,run_sheet.get_width()/8,run_sheet.get_height()/3))
            self.surf = pygame.transform.flip(self.surf, True, False)
        elif self.last_dir == "up" :
            self.surf = run_sheets[self.white].subsurface((run_sheet.get_width()/8*self.index_frame_run,run_sheet.get_height()/3*2,run_sheet.get_width()/8,run_sheet.get_height()/3))
        elif self.last_dir == "down" :
            self.surf = run_sheets[self.white].subsurface((run_sheet.get_width()/8*self.index_frame_run,run_sheet.get_height()/3*1,run_sheet.get_width()/8,run_sheet.get_height()/3))

        self.current_frame_run += 1
        if self.current_frame_run >= NB_FRAMES_SWITCH:
            self.current_frame_run = 0
            self.index_frame_run += 1
            if self.index_frame_run >= 8 :
                self.index_frame_run = 0  

    def idleAnimation(self):
        if self.last_dir == "right" :
            self.surf = idle_sheets[self.white].subsurface((idle_sheet.get_width()/4*self.index_frame_idle,idle_sheet.get_height()/3*0,idle_sheet.get_width()/4,idle_sheet.get_height()/3))
        elif self.last_dir == "left" :
            self.surf = idle_sheets[self.white].subsurface((idle_sheet.get_width()/4*self.index_frame_idle,idle_sheet.get_height()/3*0,idle_sheet.get_width()/4,idle_sheet.get_height()/3))
            self.surf = pygame.transform.flip(self.surf, True, False)
        elif self.last_dir == "up" :
            self.surf = idle_sheets[self.white].subsurface((idle_sheet.get_width()/4*self.index_frame_idle,idle_sheet.get_height()/3*2,idle_sheet.get_width()/4,idle_sheet.get_height()/3))
        elif self.last_dir == "down" :
            self.surf = idle_sheets[self.white].subsurface((idle_sheet.get_width()/4*self.index_frame_idle,idle_sheet.get_height()/3*1,idle_sheet.get_width()/4,idle_sheet.get_height()/3))

        self.current_frame_idle += 1
        if self.current_frame_idle >= NB_FRAMES_SWITCH:
            self.current_frame_idle = 0
            self.index_frame_idle += 1
            if self.index_frame_idle >= 4 :
                self.index_frame_idle = 0  

    def display(self,camera):

        display_surf.blit(self.surf, (self.rect.x - camera.x -36, self.rect.y - camera.y -32))
     

     
        #info display personnage
        display_surf.blit(self.name.surf, (self.rect.x - camera.x -15, self.rect.y - camera.y -10))   

        exp_txt = Text(str(self.blue_minerals), (0,255,255), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x - camera.x -15, self.rect.y - camera.y -15))   

        exp_txt = Text(str(self.pink_minerals), (255,20,147), 6, (0, 0))
        display_surf.blit(exp_txt.surf, (self.rect.x - camera.x -15, self.rect.y - camera.y -20))


