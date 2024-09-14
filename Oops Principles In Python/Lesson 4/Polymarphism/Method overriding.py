class x :
    def m1(self) :
        print("No param m1 of x")
    def m2(self) :
        print("No param m2 of x")
class y(x) :
    def m1(self) :
        print("No param m1 of y")
    def m3(self) :
        print("No param m3 of y")
y1 = y()
y1.m1()
y1.m2()
y1.m3()

# That means defining multiple methods with the same names with same numbers of parameters 
# (or) different parameters one method is in supperclass and another method is in subclass is known as a method overriding.
 

