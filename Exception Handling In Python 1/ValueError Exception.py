print("Begin")
i = input("Enter Fno: ")
j = input("Enter Sno: ")
try:
    x = int(i)
    y = int(j)
    z = x/y
    print(z)
except(ValueError) :
    print("Enter Numarical Values Only")
print("End")