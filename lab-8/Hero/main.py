import errors as err
import character as c

characters = []

class Menu:
    def printMenu(self):
        print("1. Create a new character")
        print("2. Create a new weapon")
        print("3. Create a new item")
        print("4. Print all characters")
        print("5. Delete a character")
        print("6. Exit the program")

    def createCharacter(self, name, sex, gameClass):
       
        for i in characters:
            if i.name == name:
                raise err.CharacterExists("This character already exists")

        if any(char.isdigit() for char in sex):
            raise err.InvalidDataFormat("Sex should cointains only letters")
        if len(name) < 4 or len(sex) < 4:
            raise  err.InvalidDataFormat("Name, sex and game class should be at least 4 letters long")
        if gameClass != "Warrior" and gameClass != "Mage" and gameClass != "Priest" and gameClass != "Rogue":
            raise err.InvalidCharacterClass("The game class should be Mage, Priest, Rogue or Warrior")
 
        character = c.Character(name,sex,gameClass)
        characters.append(character)

    def createWeapon(self, attack, characterName, weaponName):
        
        exist = False
        for i in characters:
            if i.name == characterName:
                exist = True
        if exist == False:
            raise err.CharacterNotFound("this character does not exist")
        if attack < 0:
            raise err.InvalidDataFormat("the attack should be a possitive number")  
        if type(attack) == "int":
            raise err.InvalidDataFormat("the attack should be a number")    
        if weaponName.isdigit():
            raise err.InvalidDataFormat("The weapon name should cointains only letters")
        if len(weaponName) < 4:
            raise  err.InvalidDataFormat("The weapon name should be at least 4 letters long")   
       
        weapon = c.Weapon(weaponName,attack)
        character = None
        for i in characters:
            if i.name == characterName:
                character = i
        character.mainWeapon = weapon

    def createItem(self, characterName, itemName):
        
        exist = False
        for i in characters:
            if i.name == characterName:
                exist = True
        if exist == False:
            raise err.CharacterNotFound("this character does not exist")
        if itemName.isdigit():
            raise err.InvalidDataFormat("The item name should cointains only letters")
        if len(itemName) < 4:
            raise  err.InvalidDataFormat("The item name should be at least 4 letters long")       
            

        item = c.Item(itemName)
        character = None
        for i in characters:
            if i.name == characterName:
                character = i
        character.additionalItem = item

    def printAll(self):
        for i in characters:
            i.printInfo()

    def deleteCharacter(self,name):
       
        exist = False
        for i in characters:
            if i.name == name:
                exist = True
        if exist == False:
            raise err.CharacterNotFound("this character does not exist")   
    

        for i in characters:
            if i.name == name:
                characters.remove(i)    
                     
    def run(self):
       
        while True:  
            self.printMenu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":                    
                    name = input("Enter the character name (at least 4 symbols long): ")
                    sex = input("Enter the character sex (at least 4 lettrs long): ")
                    gameClass = input("Enter the character class (Mage, Priest, Rogue, Warrior): ")
                    self.createCharacter(name,sex,gameClass)
                elif choice == "2":
                    characterName = input("Enter the character name: ")
                    weaponName = input("Enter the weapon name (at least 4 letters long): ")
                    attack = int(input("Enter an attack power for the weapon (a positive number): "))
                    self.createWeapon(attack,characterName, weaponName)
                elif choice == "3":
                    characterName = input("Enter the character name: ")
                    itemName = input("Enter the item name (at least 4 letters long: ")
                    self.createItem(characterName, itemName)
                elif choice == "4":
                    self.printAll()
                elif choice == "5":
                    name = input("Enter the character name: ")
                    self.deleteCharacter(name)
                elif choice == "6":
                    break
                else:
                    raise err.InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()
    

if __name__ == '__main__':
    menu = Menu()
    menu.run()