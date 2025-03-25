from pythoncraft.Tile import *
from pythoncraft.Character import *
import random

def mapGeneration():
    for i in range(10):
        tile = Tile((i*TILE_SIZE, 0))
        all_sprites.add(tile)
        tiles_group.add(tile)

def addCharacter():
    character = Character()
    characters.append(character)
    all_sprites.add(character)
 
def start():

    mapGeneration()


    #<---------- HERE IS THE SCRIPT INIT

    #add one character in characters array
    for i in range(10):
        addCharacter()

    #END OF THE SCRIPT INIT ------------>

    while 1:

        #<---------- HERE IS THE SCRIPT LOOP

        for character in characters:
            mylist = ["up", "down", "right", "left"]
            character.direction = random.choice(mylist)

        #END OF THE SCRIPT LOOP ------------>

        for character in characters:
            character.checkCollisions()
        
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
        camera.x = characters[0].pos.x - W_SURF/2 + ((idleSheet.get_width()/8)/2)
        camera.y = characters[0].pos.y - H_SURF/2 - ((idleSheet.get_height()/3)/2)

        #Background color of the display
        display_surf.fill((55,63,61))

        #move and display all sprites
        for entity in all_sprites:
            entity.move()
            display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        #blit the display_surf to the screen with scaling
        screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

        show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
        show_fps.display(screen)

        #update the display
        pygame.display.update()
        FramePerSec.tick(FPS)




