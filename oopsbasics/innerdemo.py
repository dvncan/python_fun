class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        
    class Engine:
        def __init__(self, n):
            self.number = n
        def start(self):
            print("Engine Started")


c = Car("ford", 2012)
e = c.Engine(12)
e.start()