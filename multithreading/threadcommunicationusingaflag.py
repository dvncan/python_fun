from threading import *;
from time import *;

class Producer:
    def __init__(self):
        #empty list of products + flag
        self.products = []
        self.ordersplaced = False
        
    def produce(self):
        #dynamically adding products to loop to produce then set flag = true
        for i in range(1,5):
            self.products.append("Product-"+str(i))
            sleep(0.1)
            print("Item Added")
        self.ordersplaced = True
        
class Consumer:
    def __init__(self, prod):
        self.prod = prod
    
    def consume(self):
        #check for flag to be true
        while self.prod.ordersplaced == False:
            #print("waiting for the orders.")
            sleep(0.2)
            
        print("Orders Shipped ", self.prod.products)
              
              
p = Producer()
c = Consumer(p)

t1= Thread(target = p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
