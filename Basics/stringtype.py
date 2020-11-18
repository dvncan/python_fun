s="  you are awesome!   "
print(s)

s1 = """you are 
the creator 
of your destiny"""
print(s1)

#indexing
print(s[2])

#repition
print(s*3)

print(len(s1))
print(len(s))

#slicing
print(s[0:5])
print(s[0:])
print(s[:8])
#-1 is the last element
print(s[-3:-1])

#step of 2 now.
print(s[0:9:2])
#-1 is the reverse order when stepping through
print(s[15::-1])
print(s[::-1])

print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(s.find("awe",0,8))
print(s.find("awe",0,len(s)))
print(s.count("a"))

print(s.replace("awesome", "super"))
print(s.upper())
print(s.lower())
print(s.title())

