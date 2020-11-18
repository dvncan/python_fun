
lst = [20,30,40,50,234]
print(type(lst))

b = bytes(lst)
print(type(b))

# error b[3] = 22

b1 = bytearray(lst)
print(b1)
print(type(b1))
b1[2] = 33
print(b1)