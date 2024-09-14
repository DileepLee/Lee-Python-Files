class x :
    def m1(self) :
        print("No param m1 of x")
    def __init__(self,msg) :
        self.msg = msg
    def __str__(self) :
        return self.msg
x1 = x("Dileep")
print(x1)
x2 = x("Python")
print(x2)
x3 = x("Dileep IT")
print(x3)