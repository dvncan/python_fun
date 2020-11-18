from threading import Thread
from time import *;


class EvenNumbers(Thread):
    def run(self, n):
        for i in range(1,n):
            print(2*i)
            
class OddNumbers(Thread):
    def run(self, n):
        for i in range(1,n):
            print(2*i-1)
            
t1 = EvenNumbers()
t2 = OddNumbers()

t1.run(6)
sleep(1)
t2.run(6)
sleep(1)

for i in range(1,101):
    print (i)