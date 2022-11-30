def getCollectionBuilder(colType):
    if colType == "list":
        def listCreator(a, b, c, d):
            list = [a, b, c, d]
            return list
        return listCreator
    elif colType == "tuple":
        def tupleCreator(a, b, c, d):
            tuple = (a, b, c, d)
            return tuple
        return tupleCreator
    elif colType == "set":
        def setCreator(a, b, c, d):
            set = {a, b, c, d}
            return set
        return setCreator
    else:
        return "Invalid input"

listBuilder = getCollectionBuilder("list")
list = listBuilder(1, 2.23, 3, "hi")
print(list)