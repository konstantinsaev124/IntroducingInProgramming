def isValidTriangle(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        return "Wrong input"

    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True

canTriangleExist = isValidTriangle

print(canTriangleExist(1,2,3))
print(isValidTriangle(20,5,30))