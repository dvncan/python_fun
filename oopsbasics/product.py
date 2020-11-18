class Product:
    
    def __init__(self):
        self.name = "iPhone"
        self.desc = "It is awesome"
        self.price = 700
    
    def display(self):
        print(self.name)
        print(self.price)
        print(self.desc)
    
p1 = Product()

p1.display()

#print(p1.name)
#print(p1.desc)
#print(p1.price)

p2 = Product()

p2.display()

#print(p2.name)
#print(p2.desc)
#print(p2.price)