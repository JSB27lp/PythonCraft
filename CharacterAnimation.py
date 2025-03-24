from head import *

class CharacterAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = idleSheet.subsurface((0,0,idleSheet.get_width()/8,idleSheet.get_height()/3))
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect()

        self.last_dir = 0

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
        self.surf = runSheet.subsurface((runSheet.get_width()/8*self.index_frame_run,runSheet.get_height()/3*0,runSheet.get_width()/8,runSheet.get_height()/3))

        if self.last_dir < 0 :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame_run += 1
        if self.current_frame_run >= NB_FRAMES_SWITCH:
            self.current_frame_run = 0
            self.index_frame_run += 1
            if self.index_frame_run >= 8 :
                self.index_frame_run = 0  

    def idleAnimation(self):
        self.surf = idleSheet.subsurface((idleSheet.get_width()/4*self.index_frame_idle,idleSheet.get_height()/3*0,idleSheet.get_width()/4,idleSheet.get_height()/3))

        if self.last_dir < 0 :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame_idle += 1
        if self.current_frame_idle >= NB_FRAMES_SWITCH:
            self.current_frame_idle = 0
            self.index_frame_idle += 1
            if self.index_frame_idle >= 4 :
                self.index_frame_idle = 0  
