from head import *
from Util.Text import *  
from World.World import *

#game variables
world = World()

world.genWorld()
world.genChests()
world.genCharacters()

for character in world.characters:
    character.updateTile(world.tiles)

#game loop
while 1: 

    for character in world.characters:
        character.pathFinding()
        character.update(world.tiles)
        character.testMinerals(world.minerals)
        character.testChests()

    world.repopMinerals()

    #print(world.characters[0].tile.x,world.characters[0].tile.y)

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

            if event.key == pygame.K_q or event.key == pygame.K_LEFT :
                world.characters[0].direction = "left"
            if event.key == pygame.K_d  or event.key == pygame.K_RIGHT :
                world.characters[0].direction = "right"
            if event.key == pygame.K_z or event.key == pygame.K_UP :
                world.characters[0].direction = "up"
            if event.key == pygame.K_s  or event.key == pygame.K_DOWN:
                world.characters[0].direction = "down"
            if event.key == pygame.K_SPACE:
                world.characters[0].direction = ""

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




