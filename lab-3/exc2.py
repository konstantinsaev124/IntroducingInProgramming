count = int(input("Enter the count of cumbers: "))
numbers = []

for i in range(0, count):
    num = int(input("Enter a number: "))
    numbers.append(num)

print(f"The sum of the numbers is: {sum(numbers)}")