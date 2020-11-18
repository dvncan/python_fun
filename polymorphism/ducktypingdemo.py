class Duck:
    def talk(self):
        print("Quack Quack")
        
class Human:
    def talk(self):
        print("Hi Hi")
        
def callTalk(obj):
    obj.talk()
    
d=Duck()
callTalk(d)

h= Human()
callTalk(h)