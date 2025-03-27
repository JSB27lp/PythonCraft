from pythoncraft.head import *

class Text(pygame.sprite.Sprite):
    def __init__(self,txt,color,size,pos, font = 'Lucida Console'):
        super().__init__()  

        my_font = pygame.font.SysFont(font, size)
        self.surf = my_font.render(txt, True, color)
        self.rect = self.surf.get_rect(center = pos)

    def display(self,surf):
        surf.blit(self.surf, self.rect)

def getPosCursor():
    mousex, mousey = pygame.mouse.get_pos()
    ratio = W_SCREEN/W_SURF     
    x = mousex/ratio
    y = mousey/ratio
    x -=5
    y -=5

    return vec(x,y)