import re 

str = "Take 1 up one 3idea. one idea5 at a t5ime"

str2 = "01-20-2019"

result = re.search(r'o\w', str)
print(result.group())

result = re.findall(r'o\w\w', str)
print(result)

#only at the beginning of the string
result = re.match(r'T\w\w', str)
print(result.group())

result = re.sub(r'one', 'two', str)
print(result)

result = re.split(r'\d+', str)
print(result)

result = re.findall(r'o\w{1,2}', str)
print(result)

#quantifiers
# +, *, ?, {m}, {m,n}

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str2)
print(result)

for i in result:
    print(i)
    
result = re.search(r'^T\w*', str)
print(result.group())
