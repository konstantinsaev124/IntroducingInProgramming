import math

class CustomError(Exception):
    pass

number = int(input("Insert a number: "))


try:
    if type(number) != int or number < 0:
        raise CustomError()
    else:     
        print(math.sqrt(number))
      
except CustomError:
    print("Invalid number")
finally: print("Good Bye")