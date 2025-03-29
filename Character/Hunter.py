from Character.Character import *

class Hunter(Character):
    def __init__(self,x,y,white,type,main):
    
        super().__init__(x,y,white,type,main)

    def action(self,world):
        self.getBackMinerals(world)

    def getBackMinerals(self,world):
        for character in world.characters:
            if round(character.x) == round(self.x) and round(character.y) == round(self.y) :
                if character.type == "Thief":
                    if self.white and not character.white:
                        self.blue_minerals+=character.blue_minerals
                        self.pink_minerals+=character.pink_minerals

                        character.blue_minerals = 0
                        character.pink_minerals = 0

                    if not self.white and character.white:
                        self.blue_minerals+=character.blue_minerals
                        self.pink_minerals+=character.pink_minerals

                        character.blue_minerals = 0
                        character.pink_minerals = 0