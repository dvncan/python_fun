#set does not allow duplicates
s={10, 20, 30, "xyz", 10, 20, 10}
print(s)
print(type(s))

s.update([88,99])
print(s)

# error print(s[0])
# error print(s[0:5])
# error print(s*3)

s.remove(30)
print(s)

f = frozenset(s)

#f.update(86)

print(s)