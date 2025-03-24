from Player import *
from Tile import *

tile = Tile((0, 0))
all_sprites.add(tile)

P1 = Player()
all_sprites.add(P1)

while 1:

    P1.checkCollisions()

    for event in pygame.event.get():
        P1.controls(event)

    if 1:
        display_surf.fill((20,18,18))
        pygame.mouse.set_visible(True) # Show cursor here
    else :
        display_surf.fill((90,192,255))
        pygame.mouse.set_visible(False) # Hide cursor here

    #ajust camera
    camera.x = P1.pos.x - W_SURF/2
    camera.y = P1.pos.y - H_SURF/2

    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    pygame.display.update()
    FramePerSec.tick(FPS)