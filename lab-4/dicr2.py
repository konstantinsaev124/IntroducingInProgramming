num = int(input("enter number: "))

numbers_list = []
dictionary = dict()

for i in range(1, num+1):
    numbers_list.append(i)

reversed_list = numbers_list[::-1]

dictionary = dict(zip(numbers_list,reversed_list))

print(dictionary)