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
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

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

camera = vec(-W_SURF/2,-H_SURF/2)

#load assets
run_sheet = pygame.image.load("assets/run.png").convert_alpha()
idle_sheet = pygame.image.load("assets/idle.png").convert_alpha()

wall_cave_img = pygame.image.load("assets/cave/wall.png").convert_alpha()
ground_cave_img = pygame.image.load("assets/cave/ground.png").convert_alpha()

TILE_SIZE = 16

all_sprites = pygame.sprite.Group()
all_characters = pygame.sprite.Group()
characters = []
all_tiles = pygame.sprite.Group()




