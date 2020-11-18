from functools import *

lst = [5,10,15,20]
#reduce to 1 number\
result = (reduce(lambda x,y: x+y, lst))
print(result)