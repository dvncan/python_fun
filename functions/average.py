def average(a,b):
    print(a)
    print(b)
    return (a+b)/2

#example of keywords that change the argument order.
result = average(b=10, a=20)
#result = average(10, 20)

print(result)