import random

class InvalidParameterError(Exception):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"Invalid class parameter: {self.name}"

class InvalidAgeError(InvalidParameterError):
    def __init__(self,name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f"Invalid parameter: {self.age}"

class InvalidSoundError(InvalidParameterError):
    def __init__(self,name, sound):
        super().__init__(name)
        self.sound = sound

    def __str__(self):
        return f"Invalid parameter: {self.sound}"


class JungleAnimal():
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

        try:
            if type(self.name) != str:
                raise InvalidParameterError(self.name)
            if type(self.age) != int:
                raise InvalidAgeError(self.name, self.age)
            if type(self.sound) != str:
                raise InvalidSoundError(self.name, self.sound)
        except InvalidParameterError as err:
            print(err)
 

    def makeSound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def dailyTask(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        self.hasError = False

        try:
            if self.age > 15:
                self.hasError = True
                raise InvalidAgeError(self.name, self.age)
            counter = 0
            for i in self.name:
                if i == "r":
                    counter += 1
            if counter < 2:
                self.hasError = True
                raise InvalidSoundError(self.name, self.sound)
        except InvalidParameterError as err:
            print(err)
    
    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def dailyTask(self, animals):
        for i in animals:
            if i.__class__.__name__ == "Human" or i.__class__.__name__ == "Lemur":
                print(f"{self.name} the Jaguar hunted down {i.name} the {i.__class__.__name__}")
                animals.remove(i)

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        self.hasError = False
        try:
            if self.age > 10:
                self.hasError = True
                raise InvalidAgeError(self.name, self.age)
            counter = 0
            for i in self.name:
                if i == "e":
                    counter += 1
            if counter < 1:
                self.hasError = True
                raise InvalidSoundError(self.name, self.sound)            
        except InvalidParameterError as err:
            print(err)

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")
    
    def dailyTask(self, fruits):
        if fruits >= 10:
            fruits -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits
        elif 0 < fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            fruits = 0
            return 0
        elif fruits <= 0:
            super().makeSound()
            super().makeSound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0
        

class Building():
    def __init__(self, type):
        self.type = type

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        self.hasError = False
    
        try:
            if self.age > 10:
                self.hasError = True
                raise InvalidAgeError(self.name, self.age)
            counter = 0
            for i in self.name:
                if i == "e":
                    counter += 1
            if counter < 1:
                self.hasError = True
                raise InvalidSoundError(self.name, self.sound)
        except InvalidParameterError as err:
            print(err)

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def dailyTask(self, animals, buildings):
        for i in range(0, len(animals)):
            hasHumans = False
            if animals[i].__class__.__name__ == "Human":
                if i == 0 and animals[1].__class__.__name__ == "Human":
                    hasHumans = True
                    continue
                if i == len(animals) - 1 and animals[i - 2]:
                    hasHumans = True
                    continue
                if animals[i - 1].__class__.__name__ == "Human" and animals[i + 1].__class__.__name__ == "Human":
                    hasHumans = True
            if hasHumans == True:
                building = Building("test")
                buildings.append(building)

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    name = names[random.randint(0, 17)]
    age = random.randint(7, 20)
    sound = sounds[random.randint(0, 8)]
    animalInt = random.randint(0, 9)
    if animalInt >= 0 and animalInt <= 3:
        animal = Lemur(name,age,sound)
        if animal.hasError == True:
            continue
        animals.append(animal)
    elif animalInt >=4 and animalInt <= 7:
        animal = Jaguar(name,age,sound)
        if animal.hasError == True:
            continue
        animals.append(animal)
    else:
        animal = Human(name,age,sound)
        if animal.hasError == True:
            continue
        animals.append(animal)

print(f"The jungle now has {len(animals)} animals")

for i in animals:
    if i.__class__.__name__ == "Human":
        i.dailyTask(animals, buildings)
    elif i.__class__.__name__ == "Jaguar":
        i.dailyTask(animals)
    else:     
        fruits = i.dailyTask(fruits)


print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)