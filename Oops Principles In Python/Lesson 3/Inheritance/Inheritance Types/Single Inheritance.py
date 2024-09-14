class x :
    def m1(self) :
        print("m1 of x")
x1 = x()
p = x1.__hash__()
print(p)
x1.m1()
