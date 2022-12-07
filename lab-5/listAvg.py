def listAvg(list, multiplayer = 1):
    sum = 0
    if type(multiplayer) != int:
        return
    for i in range(0, len(list)):
        if type(list[i]) == int or type(list[i]) == float:
            list[i] *= multiplayer
            sum += list[i]
    return sum / len(list)

print(listAvg([2,3,4,5]))