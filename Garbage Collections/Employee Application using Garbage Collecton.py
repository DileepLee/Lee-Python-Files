class Emp :
    """Emp App"""
    cnt = 0
    def __init__(self,ename,eadd,eid,esal) :
        self.ename = ename
        self.eadd = eadd
        self.eid = eid
        self.esal = esal
        Emp.cnt = Emp.cnt + 1
    def __del__(self) :
        Emp.cnt = Emp.cnt - 1
e1 = Emp("Dinesh","Dubai",7788,3000.00)
e2 = Emp("Dileep","America",7809,4000.00)
e3 = Emp("Miller","India",8767,5000.00)
e4 = Emp("Lee","Australia",3324,1000.00)
del e4
print("Total No of Employee : ",Emp.cnt)