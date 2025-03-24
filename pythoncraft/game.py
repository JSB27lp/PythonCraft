from pythoncraft.Player import *
from pythoncraft.Tile import *
from pythoncraft.Character import *

def cameraSwitch(name_character):   
    name_character_for_camera = name_character

def newCharacter(name):
    characters[name] = Character()
    all_sprites.add(characters[name])
    cameraSwitch(name)

def changeDirection(name, direction):
    characters[name].direction = direction   

def start(script_array):
    tile = Tile((0, 0))
    all_sprites.add(tile)

    player = Player()

    index_script = 0

    while 1:
        #execute the script line by line each frame
        if index_script < len(script_array):
            exec(script_array[index_script])
        index_script += 1

        #player controls like quit or zoom
        player.controls(pygame.event.get())

        #Adjust camera
        if(name_character_for_camera == ""):
            camera.x = -W_SURF/2
            camera.y = -H_SURF/2
        else:
            camera.x = characters[name_character_for_camera].pos.x - W_SURF/2
            camera.y = characters[name_character_for_camera].pos.y - H_SURF/2

        #Background color of the display
        display_surf.fill((20,18,18))

        #move and display all sprites
        for entity in all_sprites:
            entity.move()
            display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        #blit the display_surf to the screen with scaling
        screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

        #update the display
        pygame.display.update()
        FramePerSec.tick(FPS)




