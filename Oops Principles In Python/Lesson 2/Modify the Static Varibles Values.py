class Demo :
    a = 1000
    b = 2000
    def display(self) :
        print(Demo.a)
        print(Demo.b)
    def modify(self) :
        Demo.a = Demo.a+100
        Demo.b = Demo.b-100
d1 = Demo()
d1.display()
d1.modify()
d1.display()

d2 = Demo()
d2.display()
d2.modify()
d2.display()

d3 = Demo()
d3.display()
d3.modify()
d3.display()