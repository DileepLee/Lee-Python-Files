class Demo :
    def m1(self) :
        a = 1000
        b = 2000
        print(a)
        print(b)

    def m2(self) :
        c = 3000
        d = 4000
        print(c)
        print(d)
       #print(a)
       #print(b)
d1 = Demo()
d1.m1()
d1.m2()

# Here whenever we try to access the variable inside the m2 method it will give the Error MEssage.
# Because Local Variables are one mwthod it can't be accessed from outside of the method.
