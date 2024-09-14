class Cust :
    """Cust App"""
    cbname = "SBI"
    def __init__(self,cname,cadd,cacno,cbal) :
        self.cname = cname
        self.cadd = cadd
        self.cacno = cacno
        self.cbal = cbal
    def __str__(self) :
        return self.cname + " " + self.cadd + " " +str(self.cacno) + " " + str(self.cbal) + " " + self.cbname
    def deposit(self,damt) :
        self.cbal = self.cbal + damt
    def withdraw(self,wamt) :
        self.cbal = self.cbal - wamt

""" c1 = Cust("Dileep","Chittor",1001,50000.00)
print(c1)
c2 = Cust("Dinesh","Tirupati",1002,60000.00)
print(c2)
c3 = Cust("MSD","Nellore",1003,100000.00)
print(c3) """

# Here whenever we run this code it will gives type error, because its take the string type but here cbal & cacno is integer and float so it will give the error.
# So we have to modify the customer balance nad account number type.like....str(self.cacno) & str(self.cbal).
# Here we execute the all three customer lass in one time that process will use the concept of list and loops.

c1 = Cust("Dileep","Chittor",1001,50000.00)
c2 = Cust("Dinesh","Tirupati",1002,60000.00)
c3 = Cust("MSD","Nellore",1003,100000.00)

x = [c1,c2,c3]
for p in x :
    print(p)

