def customgen(x,y):
    while x<y:
        #holds x in memory creates custom ranges
        yield x
        x+=1

result = customgen(10,30)

for i in result: print(i)