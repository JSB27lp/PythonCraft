from pythoncraft.Character import *  
import noise

def start(): 

    



    #########################################
    #script for controlling algo characters#
    #########################################



    cpt_frames = 0





    while 1: #game loop



        
        
        #white part -->
        cpt_frames += 1
        if cpt_frames > 10 :
            for character in all_characters:
                if character != neo:
                    direction = random.choice(["up", "down", "right", "left"])
                    chance = random.randint(0,1)
                    if not chance : 
                        character.setDirection(direction)

            cpt_frames = 0
        #<-- black part


        '''for character_ in characters :
            collide_list = character_.collide()
            for character in collide_list : 
                character_.tryKill(character)'''
        


    #########################################
    #script for controlling your algo characters#
    #########################################
        







        #neo script
        '''
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
        

        
        '''collide_list = neo.collide()
        for character in collide_list : 
            neo.tryKill(character)'''

        for character in all_white_characters:
            if character.type=="Thief":
                collide = pygame.sprite.spritecollide(character, all_black_characters,False )
                '''for blk_char in collide :
                    if blk_char.type=="Peon":
                        blk_char.kill'''
                







        #STOP X X X X X X X X X X X X X X X X X X X X X X X X 


        #REPOP MINERALS
        nb_minerals = len(all_blue_minerals) + len(all_pink_minerals)

        #repop requirement
        if nb_minerals < 10 :

            #choisi un ground au hasard
            chance_ground = random.randint(0,len(all_grounds))
            i = 0
            for ground in all_grounds:
                i+=1
                if i == chance_ground :

                    #add mineral
                    Mineral((ground.rect.centerx,ground.rect.centery))
                    break












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
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_q or event.key == pygame.K_LEFT :
                    if neo.direction == "left":
                        neo.direction = ""
                elif event.key == pygame.K_d  or event.key == pygame.K_RIGHT :
                    if neo.direction == "right" :
                        neo.direction = ""
                elif event.key == pygame.K_z or event.key == pygame.K_UP :
                    if neo.direction == "up" :
                        neo.direction = ""
                elif event.key == pygame.K_s  or event.key == pygame.K_DOWN:
                    if neo.direction == "down" :
                        neo.direction = ""
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_q or event.key == pygame.K_LEFT :
                    neo.setDirection("left")
                if event.key == pygame.K_d  or event.key == pygame.K_RIGHT :
                    neo.setDirection("right")
                if event.key == pygame.K_z or event.key == pygame.K_UP :
                    neo.setDirection("up")
                if event.key == pygame.K_s  or event.key == pygame.K_DOWN:
                    neo.setDirection("down")

        #Background color of the display
        display_surf.fill((55,63,61))

        #move and display all sprites
        for entity in all_tiles:
            entity.move()
            entity.display(camera)
        for entity in all_chests:
            entity.move()
            entity.display(camera)
        for entity in all_pink_minerals:
            entity.move()
            entity.display(camera)
        for entity in all_blue_minerals:
            entity.move()
            entity.display(camera)
        for entity in all_characters:
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
    len_y = 5
    len_x = 10
    for y in range(len_y*-1,len_y+1):
        for x in range(len_x*-1,len_x+1):
            #add grounds and walls

            scale = 2#13
            octaves = 2#7
            lacunarity = 1.0
            persistence = 1.0
            value = noise.pnoise2(x/scale,y/scale,octaves=octaves,persistence=persistence,lacunarity=lacunarity,repeatx=len_y+1,repeaty=len_x+1,base=0)
            chance = 1
            if value <0 :
                chance = 0

            #add tiles
            tile = None
            if (not chance or y == len_y*-1 or y == len_y or x == len_x*-1 or x == len_x) and (x!=0 or y!=0) and (x!=1 or y!=0) and (x!=-1 or y!=0):
                tile = Tile((x*TILE_W, y*TILE_H), wall_cave_img)
                all_walls.add(tile)
            else :
                tile = Tile((x*TILE_W, y*TILE_H), ground_cave_img)
                all_grounds.add(tile)
                grounds.append(tile)

                #add minerals
                chance_ = random.randint(0,3)
                if not chance_ and not (x == -1 and y == 0) and not(x == 1 and y == 0):
                    Mineral((x*TILE_W, y*TILE_H))


                ratio_char = 30 #plus cest haut moins  ya des characters
                #add characters
                chance_ = random.randint(0,ratio_char*3)
                if not chance_ :
                    Thief(True,(x*TILE_W, y*TILE_H))
                    Hunter(True,(x*TILE_W, y*TILE_H))             
                chance_ = random.randint(0,ratio_char)
                if not chance_ :
                    Peon(True,(x*TILE_W, y*TILE_H))

                chance_ = random.randint(0,ratio_char*3)
                if not chance_ :
                    Thief(False,(x*TILE_W, y*TILE_H))
                    Hunter(False,(x*TILE_W, y*TILE_H))             
                chance_ = random.randint(0,ratio_char)
                if not chance_ :
                    Peon(False,(x*TILE_W, y*TILE_H))


            #add chests
            if x == -1 and y == 0:
                Chest((x*TILE_W, y*TILE_H),True)
            if x == 1 and y == 0:
                Chest((x*TILE_W, y*TILE_H),False)




mapGeneration() 
player  = Player()
neo = Thief(True,vec(-0,-0),True)
start()