from head import *

class Player():
    def __init__(self):
        super().__init__()
        self.script_line = ""  

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
                    self.script_line = textinput.value
                    textinput.value = ""

    def executeScriptLine(self,character):
        if self.script_line == "p1.left()":
            character.dir = "left"

        if self.script_line == "p1.right()":
            character.dir = "right"

        if self.script_line == "p1.up()":
            character.dir = "up"

        if self.script_line == "p1.down()":
            character.dir = "down"
            
        if self.script_line == "p1.stop()":
            character.dir = ""
 