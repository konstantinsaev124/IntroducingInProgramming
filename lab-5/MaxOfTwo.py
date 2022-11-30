def maxOfTwo(a , b):
    if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
        return
    elif (type(a) == int or type(a) == float) and (type(b) != int and type(b) != float):
        return a
    elif (type(b) == int or type(b) == float) and (type(a) != int and type(a) != float):
        return b
    elif a >= b:
        return a
    elif b > a:
        return b

print(maxOfTwo("idk",1))