from pythoncraft.head import *

class Player():
    def __init__(self):
        super().__init__()

    def controls(self,events):

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    '''a supprimer cest juste pour garder le code temporairement
    
    def executeScriptLine(self):
        if len(self.characters)>0:
            if self.script_line == "p1.left()":
                self.characters[0].dir = "left"

            if self.script_line == "p1.right()":
                self.characters[0].dir = "right"

            if self.script_line == "p1.up()":
                self.characters[0].dir = "up"

            if self.script_line == "p1.down()":
                self.characters[0].dir = "down"

            if self.script_line == "p1.stop()":
                self.characters[0].dir = ""
                
        
        if self.script_line == "Player()":
            character = Character()
            self.characters.append(character)
            all_sprites.add(character)

        self.script_line == ""
        
        '''
 