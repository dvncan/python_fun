class Programmer:
    def setName(self, n):
        self.name = n
    
    def getName(self):
        return self.name
    
    def setSal(self, m):
        self.sal = m
        
    def getSal(self):
        return self.sal
    
    def setTech(self, t):
        self.tech = t
        
    def getTech(self):
        return self.tech
        
p1 = Programmer()
p1.setName("Duncan")
p1.setSal(10000)
p1.setTech(["Java", "Python", "Spring", "Hibernate"])

print(p1.getName())
print(p1.getSal())
print(p1.getTech())