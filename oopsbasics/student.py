class Student:
    major = "CDE"
    
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
s1 = Student(1, "dunc")
s2 = Student(2, "Stu")

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(s1.rollno)
print(s2.rollno)