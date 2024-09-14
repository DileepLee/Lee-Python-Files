print("Begin")
i = input("Enter sno: ")
j = input("Entersno: ")
try:
    x = int(i)
    y = int(j)
    z = x/y
    print(z)
except(ZeroDivisionError) :
    print("sno can not be zero")
except(ValueError) :
    print("Enter Numerical Values Only")
   
except:
    print("Error Occured")
print("End")