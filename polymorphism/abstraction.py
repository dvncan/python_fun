from abc import abstractmethod
class TouchScreenLaptop():
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass
    

class HP(TouchScreenLaptop):
    
    @abstractmethod
    def scroll(self):
        TouchScreenLaptop.scroll(self)
        print("scrolling")
        
class Dell(TouchScreenLaptop):
    
    @abstractmethod
    def scroll(self):
        TouchScreenLaptop.scroll(self)
        print("scrolling")
        
class HPNotebook(HP):
    
    @abstractmethod
    def click(self):
        HP.click(self)
        print("click")
        
class DellNotebook(Dell):
    
    @abstractmethod
    def click(self):
        HP.click(self)
        print("click")
        
d = DellNotebook()
h = HPNotebook()

d.click()
h.click()
d.scroll()
h.scroll()