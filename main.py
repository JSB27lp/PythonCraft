from pythoncraft.Character import *  

def start(): 

    
    neo = Peon(True,vec(-50,-50))



    #########################################
    #script for controlling algo characters#
    #########################################



    cpt_frames = 0
    cpt_framesbis = 0


    '''for i in range(2):
        Thief(True)
        Hunter(True)
    for i in range(10):
        Peon(True)

    for i in range(2):
        Thief(False)
        Hunter(False)
    for i in range(10):
        Peon(False)'''



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
        #<-- black part


        '''for character_ in characters :
            collide_list = character_.collide()
            for character in collide_list : 
                character_.tryKill(character)'''
        


    #########################################
    #script for controlling your algo characters#
    #########################################
        






        #neo script
       
        mousex, mousey = pygame.mouse.get_pos()
        if mousex < W_SCREEN*0.4 :
            neo.setDirection("left")
        if mousex > W_SCREEN*0.6:
            neo.setDirection("right")
        
        if mousey < H_SCREEN*0.4 :
            neo.setDirection("up")
        if mousey > H_SCREEN*0.6:
            neo.setDirection("down")


        

        '''
        collide_list = neo.collide()
        for character in collide_list : 
            neo.tryKill(character)'''











        #STOP X X X X X X X X X X X X X X X X X X X X X X X X 















        #YOU DON4T NEED TO TOUCH THIS PART OF THE CODE 




        #CAREFUL : DO NOT TOUCH THIS PART OF THE CODE ---> IT IS THE GAME ENGINE


        #PLEASE DO NOT TOUCH THIS PART OF THE CODE 

















        #STOP TOUCHING THE CODE HERE











        #WHY ARE YOU STILL HERE ?









        # OK THIS PART IS REALLY USELESS FOR YOU

        # OK ? 

        #setCameraChar(neo)
        

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

def setCameraChar(char):
    camera.x = char.pos.x - W_SURF/2
    camera.y = char.pos.y - H_SURF/2

def mapGeneration():
    len_y = 4
    len_x = 7
    for y in range(len_y*-1,len_y+1):
        for x in range(len_x*-1,len_x+1):
            #add grounds and walls
            chance = random.randint(0,3)
            tile = None
            if (not chance or y == len_y*-1 or y == len_y or x == len_x*-1 or x == len_x) and (x!=0 or y!=0) and (x!=1 or y!=0) and (x!=-1 or y!=0):
                tile = Tile((x*TILE_SIZE, y*TILE_SIZE), wall_cave_img)
                all_walls.add(tile)
            else :
                tile = Tile((x*TILE_SIZE, y*TILE_SIZE), ground_cave_img)

            #add minerals
            if not((not chance or y == len_y*-1 or y == len_y or x == len_x*-1 or x == len_x) and (x!=0 or y!=0) and (x!=1 or y!=0) and (x!=-1 or y!=0)):
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