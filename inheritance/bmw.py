from abc import abstractmethod, ABC
class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        #print("Starting the car")
        pass
    
    @abstractmethod    
    def stop(self):
        #print("Stopping the car")
        pass
        
    @abstractmethod
    def drive(self):
        pass
        
class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year) #super()
        #BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
        
    def display(self):
        print(self.cruiseControlEnabled)
    
    def stop(self): #overriding
        super().stop()
        print("Button Start")
        
    def start(self): #overriding
        super().start()
        print("Button Start")
    
    def drive(self):
        BMW.drive(self)
        print("Weehoo leggo")
    
class FiveSeries(BMW):
    
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
    
    def drive(self):
        BMW.drive(self)
        print("Weehoo leggo")
        
threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()