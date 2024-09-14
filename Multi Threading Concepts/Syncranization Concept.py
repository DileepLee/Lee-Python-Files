import threading
import time
class x(threading.Thread) :
    def run(self) :
       lc.acquire()
       myfunc("Python")
       lc.release()
class y(threading.Thread) :
    def run(self) :
       lc.acquire()
       myfunc("Django")
       lc.release()
def myfunc(msg) :
    print("[hello [",msg,end="")
    time.sleep(10)
    print("] world ]")
lc = threading.Lock()
x1 = x()
y1 = y()
x1.start()
y1.start()


