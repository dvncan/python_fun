from threading import *
from asyncio.tasks import sleep

class MyThread(Thread):
    def displayNumbers(self):
        i=0
        print(current_thread().getName())
        sleep(0.05)
        while(i<10):
            print(i)
            i+=1
            
obj = MyThread()
t = Thread(target=obj.displayNumbers)
t.start()

t2 = Thread(target=obj.displayNumbers)
t2.start()

t3 = Thread(target=obj.displayNumbers)
t3.start()