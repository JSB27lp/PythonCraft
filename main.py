from pythoncraft.Character import *  

def start(): 
    #########################################
    #script for controlling your characters#
    #########################################



    cpt_frames = 0
    cpt_framesbis = 0


    for i in range(10):
        Thief(False)
        Hunter(False)
        Peon(False)

    for i in range(10):
        Thief(True)
        Hunter(True)
        Peon(True)

    while 1: #game loop


        #white part -->
        cpt_frames += 1
        if cpt_frames > 10 :
            for character in white_characters:
                direction = random.choice(["up", "down", "right", "left"])
                chance = random.randint(0,1)
                if not chance : 
                    character.setDirection(direction)

            cpt_frames = 0

        '''collide_list = neo.collide()
        for character in collide_list : 
            neo.tryKill(character)'''
        #<-- white part

        #black part -->
        cpt_framesbis += 1
        if cpt_framesbis > 10 :
            for character in black_characters:
                direction = random.choice(["up", "down", "right", "left"])
                chance = random.randint(0,1)
                if not chance : 
                    character.setDirection(direction)

            cpt_framesbis = 0
        #<-- part part


    #########################################
    #script for controlling yours characters#
    #########################################
        

























        #STOP X X X X X X X X X X X X X X X X X X X X X X X X 















        #YOU DON4T NEED TO TOUCH THIS PART OF THE CODE 




        #CAREFUL : DO NOT TOUCH THIS PART OF THE CODE ---> IT IS THE GAME ENGINE


        #PLEASE DO NOT TOUCH THIS PART OF THE CODE 

















        #STOP TOUCHING THE CODE HERE











        #WHY ARE YOU STILL HERE ?









        # OK THIS PART IS REALLY USELESS FOR YOU

        # OK ? 

        setCamera()
        

        #if quit event, exit the game
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
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

        player.play()
            
        #blit the display_surf to the screen with scaling
        screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

        show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
        show_fps.display(screen)

        #update the display
        #pygame.display.update()
        pygame.display.flip()
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
    for y in range(-11,12):
        for x in range(-19,20):
            #add grounds and walls
            chance = random.randint(0,3)
            tile = None
            if (not chance or y == -11 or y == 11 or x == -19 or x == 19) and (x!=0 or y!=0) and (x!=1 or y!=0) and (x!=-1 or y!=0):
                tile = Tile((x*TILE_SIZE, y*TILE_SIZE), wall_cave_img)
                all_walls.add(tile)
            else :
                tile = Tile((x*TILE_SIZE, y*TILE_SIZE), ground_cave_img)

            #add minerals
            if not((not chance or y == -11 or y == 11 or x == -19 or x == 19) and (x!=0 or y!=0) and (x!=1 or y!=0) and (x!=-1 or y!=0)):
                chance = random.randint(0,5)
                if not chance :
                    Mineral((x*TILE_SIZE, y*TILE_SIZE))

            #add chests
            if x == -1 and y == 0:
                Chest((x*TILE_SIZE, y*TILE_SIZE),True)
            if x == 1 and y == 0:
                Chest((x*TILE_SIZE, y*TILE_SIZE),False)




mapGeneration() 
player  = Player()
start()