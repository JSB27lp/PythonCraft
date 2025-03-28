from head import *
from Util.Text import *  
from World.World import *

#game variables
world = World()

world.mapGeneration()

#game loop
while 1: 

    for character in world.characters:
        character.move()
        character.testCollision()

    world.repopMinerals()

    #game controls
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            '''if event.key == pygame.K_q or event.key == pygame.K_LEFT :
                neo.setDirection("left")
            if event.key == pygame.K_d  or event.key == pygame.K_RIGHT :
                neo.setDirection("right")
            if event.key == pygame.K_z or event.key == pygame.K_UP :
                neo.setDirection("up")
            if event.key == pygame.K_s  or event.key == pygame.K_DOWN:
                neo.setDirection("down")'''

    #display fill
    display_surf.fill((55,63,61))

    #display sprites
    for entity in all_tiles:
        entity.display()
    for entity in all_objects:
        entity.display()
    for entity in all_characters:
        entity.display()

    #resize and blit surf on screen
    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    #show fps
    show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
    show_fps.display(screen)

    #update screen
    pygame.display.update()

    #framerate
    FramePerSec.tick(FPS)




