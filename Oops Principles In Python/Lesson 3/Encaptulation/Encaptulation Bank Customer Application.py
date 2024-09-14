class Cust :
    """Customer App"""
    cbname = "SBI"
    def __init__(self,cname,cadd,cacno,cbal) :
        self.cname = cname
        self.cadd = cadd
        self.cacno = cacno
        self.cbal = cbal
    def deposit(self,damt) :
        self.cbal = self.cbal + damt
    def withdraw(self,wamt) :
        self.cbal = self.cbal - wamt
    def display(self) :
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
        print(Cust.cbname)
c1 = Cust("Lee","Chittoor",1001,100000.00)
print(c1)
c1.deposit(50000.00)
c1.withdraw(70000.00)
c1.display()
c2 = Cust("Doss","Goa",1002,20000.00)
print(c2)
c2.deposit(5000.00)
c2.withdraw(14000.00)
c2.display()

# This is the bank related application to the customer side.
# But in this code one small problem is there that is...
# If customer withdraw above the available balance..That time it can show the USer friendly message...That process we can use the Exception handling techniques.