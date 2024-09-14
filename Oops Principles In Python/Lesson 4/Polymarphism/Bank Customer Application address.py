class Cust :
    """Cust App"""
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

c1 = Cust("Dileep","Chittor",1001,50000.00)
print(c1)
c2 = Cust("Dinesh","Tirupati",1002,60000.00)
print(c2)
c3 = Cust("MSD","Nellore",1003,100000.00)
print(c3)

# WhenEver we run this code it will gives this object address.
