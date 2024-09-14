class x :
    def __init__(self) :
        print("constructor of x")
    def m1(self) :
        print("m1 of x")
x1 = x()
print(x1)
x1.m1()
x1 = x()
print(x1)
x1.m1()

#--> That means whenever e run the code like this the first object address was deleted.
#--> Now how to know that object was deleted or not means that process we know the concept of destructor.