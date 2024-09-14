class x :
    def __init__(self):
        print("Constructor of x")
    def __del__(self) :
        print("destructor of x")
p = [x(), x(), x()]
del p[2]
del p