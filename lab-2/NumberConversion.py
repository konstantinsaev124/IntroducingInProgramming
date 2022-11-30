number = int(input('Enter a number: '))

print("Type 'hex' or 'binary'")

rand = input('Enter a word: ')
result = ""
if rand == "hex":
    while number > 0:
        currentBit = number % 16
        if currentBit == 10:
            result += 'A'
        elif currentBit == 11:
            result += 'B'
        elif currentBit == 12:
            result += 'C'
        elif currentBit == 13:
            result += 'D'
        elif currentBit == 14:
            result += 'E'    
        elif currentBit == 15:
            result += 'F'
        else :
            result += str(currentBit)

        number = number // 16
    print(result[::-1])        
     
elif rand == "binary":    
    while number > 0:
        currentBit = number % 2
        result += str(currentBit)
        number = number // 2
    print('0' + result[::-1])  
    
else:
    print("Wrong input")