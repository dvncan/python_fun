    
#has student passed, >35 .. <35 fails exam. (if fail stop.)
#average of three is the grade.. 

m = int(input("Please enter math grade: "))
p = int(input("Please enter physics grade: "))
c = int(input("Please enter chemistry grade: "))

if(m > 35 and p > 35 and c > 35):
    print("pass")
    avg = (m+p+c)/3
    if(avg <= 59):
        print("C")
    elif(avg <=69):
        print("B")
    elif(avg >= 69):
        print("A")
else:
    print("fail")
    