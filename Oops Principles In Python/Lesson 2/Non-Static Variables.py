class Demo :
    def insert(self) :
        self.a = 1000
        self.b = 2000
    def display(self) :
        print(self.a)
        print(self.b)
    def modify(self) :
        self.a = self.a+100
        self.b = self.b-100
d1 = Demo()
d1.insert()
d1.display()
d1.modify()
d1.display()

d2 = Demo()
d2.insert()
d2.display()

# That means The Non-static Variables which are modified in one object will not be modified into the other objects.