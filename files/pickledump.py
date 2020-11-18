import pickle, student

f = open("Student.dat", "wb")
s = student.Student(123, "dunc", 90)

pickle.dump(s, f)
f.close()