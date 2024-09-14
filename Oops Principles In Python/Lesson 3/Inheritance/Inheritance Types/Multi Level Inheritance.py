class x :
    def m1(self) :
        print("m1 of x")
class y(x) :
    def m2(self) :
        print("m2 of y")
class z(y) :
    def m3(self) :
        print("m3 of z")
z1 = z()
p = z1.__hash__()
print(p)
z1.m1()
z1.m2()
z1.m3()
