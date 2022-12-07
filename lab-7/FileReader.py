try:
    file = open("exc.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")
    file.close()