class X :
    a = 100
    def m1(self) :
        print("m1 of x")
class y(X) :
    b = 200
    def m2(self) :
        print("m2 of y")
    def display(self) :
        print(y.b)
        self.m2()
        print(y.a)
        self.m1()
y1 = y()
y1.display()