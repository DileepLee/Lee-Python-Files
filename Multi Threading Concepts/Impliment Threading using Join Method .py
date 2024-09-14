import time
import threading
class x(threading.Thread) :
    def run(self) :
        self.sum = 0
        for p in range(1,101) :
            self.sum = self.sum + p
class y(threading.Thread) :
    def run(self) :
        for q in range(101,201) :
            print(q)
x1 = x()
x1.start()
y1 = y()
y1.start()

# But here x1 class object isnot executed, So that process we use the concept of join method to stop the x1 thread is over.
