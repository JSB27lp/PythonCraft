from Player import *
from Character import *
from Tile import *

tile = Tile((0, 0))
all_sprites.add(tile)

player = Player()

while 1:

    player.controls(pygame.event.get())

    player.executeScriptLine()

    #ajust camera
    if len(player.characters)>0:
        camera.x = player.characters[0].pos.x - W_SURF/2
        camera.y = player.characters[0].pos.y - H_SURF/2
    else:
        camera.x = -W_SURF/2
        camera.y = -H_SURF/2

    display_surf.fill((20,18,18))

    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    screen.blit(textinput.surface, (W_SCREEN - 400, H_SCREEN - 50))

    pygame.display.update()
    FramePerSec.tick(FPS)