class Student:
    
    '''def __init__(self):
        self.__id=123 #__ makes object private
        self.__name="Duncan"
        
    def display(self): # can only access through method
        print(self.__id)
        print(self.__name)'''
    
    def setId(self, id):  # @ReservedAssignment
        self.id = id
        
    def setName(self, n):
        self.name = n
        
    def getId(self):
        return self.id
        
    def getName(self):
        return self.name
        
#s.display()

s=Student()

s.setId(123)
s.setName("dunc")

print(s.getId())
print(s.getName())

'''print(s._Student__id) # 1 _class 2 __id
print(s._Student__name)'''