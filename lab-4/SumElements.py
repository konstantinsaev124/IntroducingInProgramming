import random

n = int(input("Enter a number: "))

list  = []
result = []
list  = random.sample(range(0, 99), n)

for i in range(n):
    if (i % 2) == 0:
        result.append(list[i])
    else:
        result.append((list[i] + list[i-1]))
        result.append(list[i])

print(list)
print(result)