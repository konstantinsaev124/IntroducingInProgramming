def inputNum(list):
    sum = 0
    for i in list:
        if type(i) == int or type(i) == float:
            sum += i
        elif i.isnumeric():
            sum += int(i)
            
    print(sum)

inputNum(["3", "a", 3.14, "5"])