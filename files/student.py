class Student:
    def __init__(self, Id, n, t):
        self.Id = Id
        self.name = n
        self.testscore = t
        
    def display(self):
        print(self.Id, self.name, self.testscore)
        
