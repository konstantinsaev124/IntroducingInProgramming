import random

class Animal():
    def __init__(self, name,year, food):
        self.years = year
        self.food = food
        self.name = name

    def make_sound(self):
        pass
    def eat_food(self,quantity):
        pass

class Cat(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("Meow")

    def eat_food(self,quantity):
        foodNeeded = 10

        if quantity == 0:
            self.make_sound()
            self.make_sound()
            self.make_sound()
            self.make_sound()
            return 0
        elif foodNeeded <= quantity:
            return quantity - foodNeeded
        elif foodNeeded > quantity:
            self.make_sound()
            self.make_sound()
            return 0

class Dog(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("Bark")

    def eat_food(self,quantity, eat_quantity = 5):
        if quantity - eat_quantity < 0:
            return 0
        return quantity - eat_quantity

class Duck(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("quack")

    def eat_food(self,quantity,eat_quantity):
        self.make_sound()
        if quantity - eat_quantity < 0:
            return 0
        return quantity - eat_quantity

class Horse(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("horse sound")

    def eat_food(self,quantity):
        eat_quantity = 15
        if quantity < 8:
            return 0, quantity
        if quantity - eat_quantity < 15:
            eat_quantity = 8
            return quantity - eat_quantity, eat_quantity
        else:
            return quantity - eat_quantity, eat_quantity

cat = Cat("ivan", 3, "chicken")
cat1 = Cat("petar", 5, "beef")
dog = Dog("pesho", 6, "pork")
dog1 = Dog("mariqn", 4, "beef")
dog2 = Dog("spas", 7, "chicken")
duck = Duck("gosho", 4, "chicken")
horse = Horse("boiko", 6, "pork")
horse1 = Horse("denis", 5, "grass")
duck1 = Duck("ivailo", 7, "grass")
duck2 = Duck("krasi", 8, "grass")

animals = [cat,cat1,dog,dog1,dog2,duck,horse,duck1,duck2,horse1]


for i in animals:
    print("============================================================")
    food = {"fish": 45, "dogFood":44, "duckFood":50, "grass":120}
    for k in range(0,10):
        if type(i) == Cat:
            foodQuantity = food["fish"]
            if foodQuantity < 0:
                foodQuantity = 0
            if(foodQuantity < 10):
                print(f"{i.name} the Cat jsut ate {foodQuantity} {list(food.keys())[0]}, there's {i.eat_food(foodQuantity)} left.")
            else:
                print(f"{i.name} the Cat jsut ate 10 {list(food.keys())[0]}, there's {i.eat_food(foodQuantity)} left.")
            food["fish"] -= 10
        elif type(i) == Dog:
            foodQuantity = food["dogFood"]
            if foodQuantity < 0:
                foodQuantity = 0
            if(foodQuantity < 5):
                print(f"{i.name} the Dog jsut ate {foodQuantity} {list(food.keys())[1]}, there's {i.eat_food(foodQuantity)} left.")
            else:
                print(f"{i.name} the Dog jsut ate 5 {list(food.keys())[1]}, there's {i.eat_food(foodQuantity)} left.")
            food["dogFood"] -= 5
        elif type(i) == Duck:
            foodQuantity = food["duckFood"]
            eat_quantity = random.randint(1,9)
            if eat_quantity > foodQuantity:
                eat_quantity = foodQuantity
            print(f"{i.name} the Duck jsut ate {eat_quantity} {list(food.keys())[2]}, there's {i.eat_food(foodQuantity,eat_quantity)} left.")
            food["duckFood"] -= eat_quantity
        elif type(i) == Horse:
            foodQuantity = food["grass"]
            result = i.eat_food(foodQuantity)
            print(f"{i.name} the Horse jsut ate {result[1]} {list(food.keys())[3]}, there's {result[0]} left.") 
            food["grass"] -= result[1] 