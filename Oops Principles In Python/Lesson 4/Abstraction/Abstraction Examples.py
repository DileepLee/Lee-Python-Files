class x :
    a = 1000
    def m1(self) :
        print("m1 of x")
    def display(self) :
        print(x.a)
        self.m1()
x1 = x()
x1.display()
print(x.a)
x1.m1()