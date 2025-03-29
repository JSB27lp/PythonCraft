from Character.Character import *

class Peon(Character):
    def __init__(self,x,y,white,type,main):
    
        super().__init__(x,y,white,type,main)

    def action(self,world):
        self.testMinerals()

    def testMinerals(self):

        if self.tile.mineral != None:
            if self.tile.mineral.type == "blue":
                self.blue_minerals+=1
            if self.tile.mineral.type == "pink":
                self.pink_minerals+=1

            self.tile.mineral.kill()
            self.tile.mineral = None