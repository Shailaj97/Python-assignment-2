#Custom Error using Exception or BaseException class using message to handle at least two of the cases.

class Error(Exception):
    #Base class for other exceptions
    pass

class ValueTooLargeError(Error):
    pass

class ValueTooSmallError(Error):
    pass

number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")