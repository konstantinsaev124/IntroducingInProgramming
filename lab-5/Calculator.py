def divide(a, b):
    return a / b
def multiply(a, b):
    return a * b
def add(a, b):
    return a + b
def substract(a, b):
    return a - b

print("Operations: \n 1.Divide \n 2.Multiply \n 3.Add \n 4.Substract")

choice = int(input("Select a number: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a, " / ", b, " = ", divide(a, b))
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print(a, " * ", b, " = ", multiply(a, b))
elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a, " + ", b, " = ", add(a, b))
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a, " - ", b, " = ", substract(a,b)) 
else:
    print("Invalid number")   