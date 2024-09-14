class book :
    def bd1(self) :
        print("This is details of book")
class other :
    def od2(self) :
        print("This is details of other")
class normal(book,other) :
    def nd3(self) :
        print("This is details of normal")
normal1 = normal()
p = normal1.__hash__()
print(p)
normal1.bd1()
normal1.od2()
normal1.nd3()
