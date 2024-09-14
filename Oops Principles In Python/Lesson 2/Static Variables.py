class Demo :
    a = 1000
    b = 2000
    def display(self) :
        print(Demo.a)
        print(Demo.b)
d1 = Demo()
print(d1)
d1.display()
print(Demo.a)
print(Demo.b)
print(d1.a)
print(d1.b)
