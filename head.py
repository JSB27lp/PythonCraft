import pygame
import random
import sys


#init app
pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
vec = pygame.math.Vector2 #2 for two dimensional
FramePerSec = pygame.time.Clock()
pygame.mouse.set_visible(True) # Hide cursor here
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
pygame.display.set_caption("PythonCraft")

#set global variable
FPS = 60
DEADZONE = 0.3#for joystick
NB_FRAMES_SWITCH = 8

OFFSET_X = 16
OFFSET_Y = 20

ROWS = 21
COLS = 39
 
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
run_sheet_white = pygame.image.load("assets/run.png").convert_alpha()
idle_sheet_white = pygame.image.load("assets/idle.png").convert_alpha()
run_sheet_black = pygame.image.load("assets/run_black.png").convert_alpha()
idle_sheet_black = pygame.image.load("assets/idle_black.png").convert_alpha()
run_sheets = [run_sheet_black,run_sheet_white]
idle_sheets = [idle_sheet_black,idle_sheet_white]

TILE_SIZE = 16
wall_cave_img = pygame.image.load("assets/cave/wall.png").convert_alpha()
wall_cave_img = pygame.transform.scale(wall_cave_img,(TILE_SIZE,TILE_SIZE))
ground_cave_img = pygame.image.load("assets/cave/ground.png").convert_alpha()
ground_cave_img = pygame.transform.scale(ground_cave_img,(TILE_SIZE,TILE_SIZE))

mineral_sheet = pygame.image.load("assets/cave/gems.png").convert_alpha()

chest_img = pygame.image.load("assets/chest.png").convert_alpha()

#sprites groups
all_characters = pygame.sprite.Group()
all_tiles = pygame.sprite.Group()
all_minerals = pygame.sprite.Group()
all_chests = pygame.sprite.Group()





