from rectangleArea import rectangle
from triangleArea import triangle
from squareArea import square
from rombArea import romb
from trapezoidArea import trapezoid

figure = str(input("Enter a figure: "))

if figure == "rectangle":
   a = float(input("Enter a: "))
   b = float(input("Enter b: "))
   print(f"The area is {rectangle(a, b)}")
elif figure == "triangle":
    a = float(input("Enter a: ")) 
    b = float(input("Enter b: ")) 
    print(f"The area is {triangle(a,b)}")
elif figure == "square":
    a = float(input("Enter a: "))
    print(f"The area is {square(a)}")
elif figure == "romb":
    a = float(input("Enter a: ")) 
    print(f"The area is {romb(a)}")    
elif figure == "trapezoid":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    h = float(input("Enter h: "))
    print(f"The area is {trapezoid(a, b, h)}")
