class Test :
    def m1(self) :
        print("No param m1")
    def m1(self,a) :
        print("One param m1")
    def m1(self,a,b) :
        print("Two param m1")
t1 = Test()
t1.m1(1000,2000)

# But we pass the one value like....
t1.m1(1000)
#---> it will give error message, because whenever we define multiple method
#---> by default python interpriter is recognising only the last defined method of the class.
