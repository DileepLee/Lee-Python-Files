class x :
    def m1(self) :
        print("m1 of x")
class y(x) :
    def m2(self) :
        print("m2 of y")
class z(x) :
    def m3(self) :
        print("m3 of z")
y1 = y()
p = y1.__hash__()
print(p)
y1.m1()
y1.m2()


