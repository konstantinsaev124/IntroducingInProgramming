def palindrome(string):
    reversed_string = string[::-1]
    status=1
    if(string!=reversed_string):
        status=0
    return status


string = input("Enter input: ")
status= palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Not a palindrome")