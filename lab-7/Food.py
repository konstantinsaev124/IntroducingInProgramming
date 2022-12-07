class InvalidParameterError(Exception):
    pass

class NutrientError(Exception):
    pass

class InvalidFoodError(Exception):
    pass

class Food():
    def __init__(self, carbs, protein, fats, salt):
        self.carbs = carbs
        self.protein = protein
        self.fats = fats
        self.salt = salt
        self.hasError = False

        try:
            if type(self.carbs) != float or type(self.fats) != float or type(self.protein) != float or type(self.salt) != float:
                self.hasError = True
                raise InvalidParameterError()
            if sum([self.carbs, self.protein, self.fats, self.salt]) > 100:
                self.hasError = True
                raise NutrientError()
            if sum([self.carbs, self.salt, self.fats, self.protein]) == 0:
                self.hasError = True
                raise InvalidFoodError()
        except InvalidParameterError:
            print("All fields must be float")
        except NutrientError:
            print("Too many calories")
        except InvalidFoodError:
            print("At least one of the fields must be different from 0")
 
        
    def printLabel(self):
        print(f"{self.__class__.__name__} ({self.carbs}) ({self.protein}) ({self.fats}) ({self.salt})")

for i in range(0,120,10):
    food = Food(float(i), float(i), float(i), float(i))
    if food.hasError == False:
        food.printLabel()

