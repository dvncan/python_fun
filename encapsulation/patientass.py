class Patient():
        
    def setId(self, i):
        self.id = i
        
    def setName(self, n):
        self.name = n
        
    def setSsn(self, m):
        self.ssn = m
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getSsn(self):
        return self.ssn
    

p = Patient()

p.setId(123)
p.setName("george")
p.setSsn(12345)

print(p.getId())
print(p.getName())
print(p.getSsn())