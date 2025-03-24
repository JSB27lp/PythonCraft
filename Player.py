from Character import *

class Player(Character):
    def __init__(self):
        super().__init__()  

    def controls(self,events):
        textinput.update(events)

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    print(textinput.value)
                    textinput.value = ""
 