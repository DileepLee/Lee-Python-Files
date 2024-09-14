i = input("Enter positive Number : ")
x = int(i)
if x < 10 :
    print("Given Number is 1 digit")
elif x < 100 :
    print("Given number is 2 digits")
elif x < 1000 :
    print("Given number is 3 digits")
elif x < 100000:
    print("Given number is 4 digits")
else:
    print("Given Number >=5 digits")
