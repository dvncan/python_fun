tpl = (40, 50, "xyz")
print(tpl)

tpl = (40, )
print(tpl)

tpl = 40
print(type(tpl))

tpl = (40, 50, 40, "xyz")
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("xyz"))

lst = [67, 34, "xyz"]
print(type(lst))
tpl1 = tuple(lst)
print(tpl1)
print(type(tpl1))