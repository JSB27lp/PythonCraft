from pythoncraft.Tile import * #X ignore this line and do not touchX X X X X X X 
from pythoncraft.Character import * #X ignore this line and do not touchX X X X X X X 
from pythoncraft.Util import * #X ignore this line and do not touchX X X X X X X X X X 
 
def start(): #X ignore this line and do not touchX X X X X X X X X X X X X 

    mapGeneration() #X ignore this line and do not touchX X X X X X X X X X X X 





    

    #init before loop

    #white part -->
    neo = Hacker(False)
    addCharacter(neo)

    for i in range(10):
        character = Hacker(True)
        addCharacter(character)

        character = Agent(False)
        addCharacter(character)

        character = Peon(True)
        addCharacter(character)
    #<-- white part

    #black part -->
    #<-- black part

    cpt_frames = 0

    while 1: #game loop

        cpt_frames += 1

        #white part -->
        if cpt_frames > 10 :
            for character in characters:
                direction = random.choice(["up", "down", "right", "left"])
                chance = random.randint(0,1)
                if not chance : 
                    character.setDirection(direction)

            cpt_frames = 0

        collide_list = neo.collide()
        for character in collide_list : 
            neo.tryKill(character)
        #<-- white part

        #black part -->
        #<-- part part

        

        

























        #STOP X X X X X X X X X X X X X X X X X X X X X X X X 















        #YOU DON4T NEED TO TOUCH THIS PART OF THE CODE 




        #CAREFUL : DO NOT TOUCH THIS PART OF THE CODE ---> IT IS THE GAME ENGINE


        #PLEASE DO NOT TOUCH THIS PART OF THE CODE 

















        #STOP TOUCHING THE CODE HERE











        #WHY ARE YOU STILL HERE ?








        #START game internal mechanics

        for character in all_characters:
            character.exp += 1

        #END game internal mechanics




        # OK THIS PART IS REALLY USELESS FOR YOU

        # OK ? 

        setCamera()
        

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

        #Background color of the display
        display_surf.fill((55,63,61))

        #move and display all sprites
        for entity in all_sprites:
            entity.move()
            entity.display(camera)
            
        #blit the display_surf to the screen with scaling
        screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

        show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
        show_fps.display(screen)

        #update the display
        pygame.display.update()
        FramePerSec.tick(FPS)

def setCamera():
    mousex, mousey = pygame.mouse.get_pos()
    if mousex < W_SCREEN*0.2 :
        camera.x -= 3
    if mousex > W_SCREEN*0.8:
        camera.x += 3
    
    if mousey < H_SCREEN*0.2 :
        camera.y -= 3
    if mousey > H_SCREEN*0.8:
        camera.y += 3

def mapGeneration():
    for i in range(10):
        chance = random.randint(0,1)
        if chance :
            tile = Tile((i*TILE_SIZE, 0), wall_cave_img)
        else : 
            tile = Tile((i*TILE_SIZE, 0), ground_cave_img)

        all_sprites.add(tile)
        all_tiles.add(tile)

def addCharacter(character):
    characters.append(character)
    all_characters.add(character)
    all_sprites.add(character)


start()