from pythoncraft.Tile import *
from pythoncraft.Character import *
 
def start():
    all_sprites = pygame.sprite.Group()
    characters = []

    tile = Tile((0, 0))
    all_sprites.add(tile)

    character = Character()
    characters.append(character)
    all_sprites.add(character)

    while 1:

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #<-- HERE IS THE SCRIPT

        #END OF THE SCRIPT -->

        #Adjust camera
        if(len(characters)==0):
            camera.x = -W_SURF/2
            camera.y = -H_SURF/2
        else:
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




