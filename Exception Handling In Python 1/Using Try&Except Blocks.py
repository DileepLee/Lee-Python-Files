print("Begin")
i = input("Enter first Number: ")
j = input("Enter Second Number: ")
x = int(i)
y = int(j)
try :
    z = x/y 
    print(z)
except(ZeroDivisionError) :
    print("Number can be Zero")
print("End")

# Whenever we entered zero the try block has to ba take except block will take the controles to find that error to print the error message...
# Whenever we enter the alphabates in the input value it will display the output is VAlue Error...