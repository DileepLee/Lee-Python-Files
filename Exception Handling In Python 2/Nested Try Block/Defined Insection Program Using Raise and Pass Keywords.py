class ValueTooSmallError(Exception) :
    pass
class ValueTooLargeError(Exception) :
    pass
number = 10
while True :
    try:
        i_num = int(input("Enter a Number: "))
        if i_num < number :
            raise ValueTooSmallError
        elif i_num > number :
            raise ValueTooLargeError
        break
    except(ValueTooSmallError) :
        print("This Value is too samll, try Again!")
    except(ValueTooLargeError) :
        print("This VAlue is Too Large, try Again!")
print("Congratulations! You Guessed it currectly.")