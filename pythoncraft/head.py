import pygame
from pygame.locals import *
import random
import sys

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

vec = pygame.math.Vector2 #2 for two dimensional

ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((1920, 1080))
infoObject = pygame.display.Info()
W_SCREEN = infoObject.current_w
H_SCREEN = infoObject.current_h

W_SURF = 640
H_SURF = 360
display_surf = pygame.surface.Surface((W_SURF, H_SURF))

NB_FRAMES_SWITCH = 8

pygame.mouse.set_visible(True) # Hide cursor here
pygame.display.set_caption("PythonCraft")

runSheet = pygame.image.load("assets/run.png").convert_alpha()
idleSheet = pygame.image.load("assets/idle.png").convert_alpha()

tilesetSheet = pygame.image.load("assets/tileset.png").convert_alpha()

all_sprites = pygame.sprite.Group()
characters = []
camera = vec(0,0)




