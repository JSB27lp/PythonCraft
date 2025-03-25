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
runSheet = pygame.image.load("assets/run.png").convert_alpha()
idleSheet = pygame.image.load("assets/idle.png").convert_alpha()

tilesetSheet1 = pygame.image.load("assets/tileset/1.png").convert_alpha()
tilesetSheet2 = pygame.image.load("assets/tileset/2.png").convert_alpha()
tilesetSheet3 = pygame.image.load("assets/tileset/3.png").convert_alpha()
tilesetSheet4 = pygame.image.load("assets/tileset/4.png").convert_alpha()
tilesetSheet5 = pygame.image.load("assets/tileset/5.png").convert_alpha()
tilesetSheet6 = pygame.image.load("assets/tileset/6.png").convert_alpha()

TILE_SIZE = 16


class Text(pygame.sprite.Sprite):
    def __init__(self,txt,color,size,pos, font = 'Lucida Console'):
        super().__init__()  

        my_font = pygame.font.SysFont(font, size)
        self.surf = my_font.render(txt, True, color)
        self.rect = self.surf.get_rect(center = pos)

    def display(self,surf):
        surf.blit(self.surf, self.rect)


