class x :
    __a = 1000
    def __m1(self) :
        print("m1 of x")
    def display(self) :
        print(x.__a)
        self.__m1()
x1 = x()
x1.display()
print(x.__a)  #--> HEre it will give Attribute Error. 
                #-->Because The same class thed=se priperty __a & __m1 can be accessed in display method.
                #--> But can't be access this hidden property from the class x from outside of the class.
                #--> That is nothing but (x.__a) will give error and x1.__m1() method will also give Error.
                #--> This is nothing but implimentation of abstraction Oops principles in python language.
x1.__m1()