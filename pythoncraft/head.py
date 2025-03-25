import pygame
from pygame.locals import *
import random
import sys

#init app
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
vec = pygame.math.Vector2 #2 for two dimensional
FramePerSec = pygame.time.Clock()
pygame.mouse.set_visible(True) # Hide cursor here
pygame.display.set_caption("PythonCraft")
camera = vec(0,0)

#set global variable for character
ACC = 0.5
FRIC = -0.12
FPS = 60
NB_FRAMES_SWITCH = 8
 
#set screen
screen = pygame.display.set_mode((1920, 1080))
infoObject = pygame.display.Info()
W_SCREEN = infoObject.current_w
H_SCREEN = infoObject.current_h

#set surface display
W_SURF = 640
H_SURF = 360
display_surf = pygame.surface.Surface((W_SURF, H_SURF))

#load assets
run_sheet = pygame.image.load("assets/run.png").convert_alpha()
idle_sheet = pygame.image.load("assets/idle.png").convert_alpha()

wall_cave_img = pygame.image.load("assets/cave/wall.png").convert_alpha()
ground_gave_img = pygame.image.load("assets/cave/ground.png").convert_alpha()

TILE_SIZE = 16

all_sprites = pygame.sprite.Group()
characters = []
tiles_group = pygame.sprite.Group()

class Text(pygame.sprite.Sprite):
    def __init__(self,txt,color,size,pos, font = 'Lucida Console'):
        super().__init__()  

        my_font = pygame.font.SysFont(font, size)
        self.surf = my_font.render(txt, True, color)
        self.rect = self.surf.get_rect(center = pos)

    def display(self,surf):
        surf.blit(self.surf, self.rect)


