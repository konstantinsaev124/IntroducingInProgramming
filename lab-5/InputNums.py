def inputNum(n):
    list = []
    for i in range(0,n):

        element = input("Enter a number: ")

        if element.isnumeric():
            list.append(int(element))
            
    print(list)

inputNum(3)