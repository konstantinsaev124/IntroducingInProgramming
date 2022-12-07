def rectangle(lenght, width):
    return lenght * width
def triangle(base, height):
    return (base * height) / 2
def square(side):
    return side * side

n = str(input("Enter a figure: "))

if n == "rectangle":
    w = int(input("Enter width: "))
    l = int(input("Enter lenght: "))
    print(rectangle(w, l))
elif n == "triangle":
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    print(triangle(b, h))
elif n == "square":
    s = int(input("Enter side: "))
    print(square(s))    