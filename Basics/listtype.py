lst = [10,20,"duncan", -10, 30.5]
print(lst)

print(lst[3])

#slicing -- there is no fifth element so it stops at [4]
print(lst[3:5])
print(lst[::-1])
print(lst*4)

print(len(lst))

lst.append(40)
print(lst)

lst.remove('duncan')
print(lst)
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst[::-1]
print(lst)