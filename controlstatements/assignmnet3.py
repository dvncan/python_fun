x = int(input("Please enter a number: "))

for i in range(1,x+1):
    if(i%10==0):continue
    print(i)
    if(i>100):break
    i+=1
    
