def listManipulator(list,n):
    for i in range(0, len(list)):
        if list[i] > n:
            list[i] = 0
    print(list)

listManipulator([0,1,2,3,4,5], 4)