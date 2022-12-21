import Operations

a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation = input("Enter operation: ")

if operation == "add":
    print(Operations.plus(a, b))

elif operation == "subtract":
    print(Operations.minus(a, b))

elif operation == "division":
    print(Operations.devide(a, b))

elif operation == "multiply":
    print(Operations.multiply(a, b))

else:
    print("Invalid operation!")