from Player import *
from Tile import *

tile = Tile((0, 0))
all_sprites.add(tile)

P1 = Player()
all_sprites.add(P1)

while 1:

    P1.checkCollisions()

    events = pygame.event.get()
    for event in events:

        P1.controls(event)
    
    textinput.update(events)
    
    display_surf.fill((20,18,18))

    #ajust camera
    camera.x = P1.pos.x - W_SURF/2
    camera.y = P1.pos.y - H_SURF/2

    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    display_surf.blit(textinput.surface, (10, 10))

    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    pygame.display.update()
    FramePerSec.tick(FPS)