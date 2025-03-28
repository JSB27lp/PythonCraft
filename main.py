from head import *
from Util.Text import *  
from World.World import *

def joystickControls(world):
    if pygame.joystick.get_count()>0:

        axis_x = joysticks[0].get_axis(0)
        axis_y = joysticks[0].get_axis(1)

        if axis_x < -1 * DEADZONE:
            world.characters[0].direction = "left"
        elif axis_x > DEADZONE:
            world.characters[0].direction = "right"
        elif axis_y < -1 * DEADZONE:
            world.characters[0].direction = "up"
        elif axis_y > DEADZONE:
            world.characters[0].direction = "down"
        else:
            world.characters[0].direction = ""

def keyboardControls(world):
    #keyboard controls
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_q or event.key == pygame.K_LEFT :
                if world.characters[0].direction == "left":
                    world.characters[0].direction = ""
            elif event.key == pygame.K_d  or event.key == pygame.K_RIGHT :
                if world.characters[0].direction == "right" :
                    world.characters[0].direction = ""
            elif event.key == pygame.K_z or event.key == pygame.K_UP :
                if world.characters[0].direction == "up" :
                    world.characters[0].direction = ""
            elif event.key == pygame.K_s  or event.key == pygame.K_DOWN:
                if world.characters[0].direction == "down" :
                    world.characters[0].direction = ""
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

def mouseControls(world):
    mousex, mousey = pygame.mouse.get_pos()

    ratio = W_SCREEN/W_SURF

    mousex/=ratio
    mousey/=ratio

    mousex-=OFFSET_X
    mousey-=OFFSET_Y

    mousex/=TILE_SIZE
    mousey/=TILE_SIZE

    mousex=round(mousex)
    mousey=round(mousey)

    if mousex >-1 and mousex < COLS and mousey >-1 and mousey < ROWS :
        
        print(mousex, mousey)

        cost = np.ones((5, 10), dtype=np.int8, order="F")
        graph = tcod.path.SimpleGraph(cost=cost, cardinal=2, diagonal=3)
        pf = tcod.path.Pathfinder(graph)
        pf.add_root((2, 4))
        pf.path_to((3, 7)).tolist()

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
        character.move(world)
        character.action(world)
        
        character.testChests()

    world.repopMinerals()
    

    joystickControls(world)
    keyboardControls(world)
    mouseControls(world)


    #display fill
    display_surf.fill((55,63,61))

    #display sprites
    for entity in all_tiles:
        entity.display()
    for entity in all_minerals:
        entity.display()
    for entity in all_chests:
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





