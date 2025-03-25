from pythoncraft.Tile import * #ignore this line and do not touch
from pythoncraft.Character import * #ignore this line and do not touch
import random #ignore this line and do not touch
 
def start(): #ignore this line and do not touch

    mapGeneration() #ignore this line and do not touch


    #add one character in characters array
    for i in range(10):
        addCharacter()


    while 1: 


        for character in characters:
            mylist = ["up", "down", "right", "left"]
            character.direction = random.choice(mylist)






        #STOP















        #YOU DON4T NEED TO TOUCH THIS PART OF THE CODE 




        #CAREFUL : DO NOT TOUCH THIS PART OF THE CODE ---> IT IS THE GAME ENGINE


        #PLEASE DO NOT TOUCH THIS PART OF THE CODE 

















        #STOP TOUCHING THE CODE HERE











        #WHY ARE YOU STILL HERE ?








        #START game internal mechanics

        for character in characters:
            character.checkCollisions()

        #END game internal mechanics




        # OK THIS PART IS REALLY USELESS FOR YOU

        # OK ? 




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
        camera.x = characters[0].pos.x - W_SURF/2 + ((idle_sheet.get_width()/8)/2)
        camera.y = characters[0].pos.y - H_SURF/2 - ((idle_sheet.get_height()/3)/2)

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

def mapGeneration():
    for i in range(10):
        chance = random.randint(0,1)
        if chance :
            tile = Tile((i*TILE_SIZE, 0), wall_cave_img)
        else : 
            tile = Tile((i*TILE_SIZE, 0), ground_cave_img)

        all_sprites.add(tile)
        tiles_group.add(tile)

def addCharacter():
    character = Character()
    characters.append(character)
    all_sprites.add(character)


start()