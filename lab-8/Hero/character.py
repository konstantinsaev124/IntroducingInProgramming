class Character:
    def __init__(self, name, sex, gameClass):
        self.name = name
        self.sex = sex
        self.gameClass = gameClass
        self.mainWeapon = None
        self.additionalItem = None

    def printInfo(self):
        if self.mainWeapon == None and self.additionalItem != None:
            print(f"{self.name}({self.sex}) the {self.gameClass} with no main weapon and item {self.additionalItem.name}")
        elif self.mainWeapon != None and self.additionalItem == None:
            print(f"{self.name}({self.sex}) the {self.gameClass} with main weapon {self.mainWeapon.name} and no item")
        elif self.mainWeapon == None and self.additionalItem == None:
            print(f"{self.name}({self.sex}) the {self.gameClass} with no main weapon and no item")
        else:
            print(f"{self.name}({self.sex}) the {self.gameClass} with main weapon {self.mainWeapon.name} and item {self.additionalItem.name}")
class Item:
     def __init__(self,name):
        self.durability = 100
        self.name = name

class Weapon(Item):
    def __init__(self, name, attack):
        super().__init__(name)
        self.durability = 100
        self.attack = attack
       