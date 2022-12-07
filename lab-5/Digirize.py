def digitize(n):
    if type(n) != int:
        print("Wrong input")
        return
    
    string = str(n)
    
    list = []


    for i in string:
        list.append(int(i))
        
    return tuple(list)

print(digitize(1234))