primeFlag = True
x = int(input("Please enter a number: "))
i=2
while i < x-1:
    if(x%i == 0): primeFlag=False
    i+=1
    
if(primeFlag):print("Prime Number")
else: print("Not a prime number")