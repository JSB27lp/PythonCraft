from Player import *
from Character import *
from Tile import *

tile = Tile((0, 0))
all_sprites.add(tile)

p1 = Character()
all_sprites.add(p1)

player = Player()

while 1:

    player.controls(pygame.event.get())

    player.executeScriptLine(p1)
    
    p1.checkCollisions()

    #ajust camera
    camera.x = p1.pos.x - W_SURF/2
    camera.y = p1.pos.y - H_SURF/2

    display_surf.fill((20,18,18))

    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    display_surf.blit(textinput.surface, (10, 10))

    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    pygame.display.update()
    FramePerSec.tick(FPS)