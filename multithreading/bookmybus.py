from threading import *

class BookMyBus:
    
    def __init__(self, aS1):
        self.availableSeats = aS1
        #self.l = Lock()
        self.l = Semaphore()
    
    def buy(self, seatsReq):
        self.l.acquire()
        print("total seats: ", self.availableSeats)
        if(self.availableSeats >= seatsReq):
            print("confirming seat")
            print("processing payment")
            print("printing ticket")
            self.availableSeats-=seatsReq
        else:
            print("sorry no seats")
        self.l.release()
        
obj = BookMyBus(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(2,))

t1.start()
t2.start()
t3.start()