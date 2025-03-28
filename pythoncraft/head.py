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

#set global variable for character
ACC = 0.5
FRIC = -0.3
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
run_sheet_black = pygame.image.load("assets/run_black.png").convert_alpha()
idle_sheet_black = pygame.image.load("assets/idle_black.png").convert_alpha()
run_sheets = [run_sheet_black,run_sheet]
idle_sheets = [idle_sheet_black,idle_sheet]

RATIO_TILE = 1.4

wall_cave_img = pygame.image.load("assets/cave/wall.png").convert_alpha()
wall_cave_img = pygame.transform.scale(wall_cave_img,(wall_cave_img.get_width()/RATIO_TILE,wall_cave_img.get_height()/RATIO_TILE))
ground_cave_img = pygame.image.load("assets/cave/ground.png").convert_alpha()
ground_cave_img = pygame.transform.scale(ground_cave_img,(ground_cave_img.get_width()/RATIO_TILE,ground_cave_img.get_height()/RATIO_TILE))

mineralSheet = pygame.image.load("assets/cave/gems.png").convert_alpha()

chest_img = pygame.image.load("assets/chest.png").convert_alpha()

#game variables
TILE_W = wall_cave_img.get_width()/RATIO_TILE
TILE_H = wall_cave_img.get_height()/RATIO_TILE

all_sprites = pygame.sprite.Group()

all_white_characters = pygame.sprite.Group()
white_characters = []
all_black_characters = pygame.sprite.Group()
black_characters = []
all_characters = pygame.sprite.Group()
characters = []

all_tiles = pygame.sprite.Group()
all_walls = pygame.sprite.Group()
all_grounds = pygame.sprite.Group()
grounds = []

all_blue_minerals = pygame.sprite.Group()
all_pink_minerals = pygame.sprite.Group()

all_chests = pygame.sprite.Group()




