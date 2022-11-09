num = int(input("Enter a number:"))

if num > 1:
    if num == 2:
        print("The number is prime")
    elif num == 3:
        print("The number is prime")
    elif num % 2 == 0 or num % 3 == 0:
        print("The number isn't prime")
    else:
        print("The number is prime")
else:
    print("The number isn't prime")