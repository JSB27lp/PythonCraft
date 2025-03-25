from pythoncraft.Tile import *
from pythoncraft.Character import *
import random

all_sprites = pygame.sprite.Group()
characters = []

def mapGeneration():
    tile = Tile((0, 0))
    all_sprites.add(tile)

def addCharacter():
    character = Character()
    characters.append(character)
    all_sprites.add(character)
 
def start():

    mapGeneration()


    #<---------- HERE IS THE SCRIPT
    #add one character in characters array
    addCharacter()

    while 1:

        mylist = ["up", "down", "right", "left"]
        characters[0].direction = random.choice(mylist)
        #END OF THE SCRIPT ------------>

        
        #if quit event, exit the game
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #Adjust camera
        camera.x = characters[0].pos.x - W_SURF/2
        camera.y = characters[0].pos.y - H_SURF/2

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




