from datetime import *

d = date(2018,7,5)
t = time(21,4)

dt = datetime.combine(d,t)

print(dt)