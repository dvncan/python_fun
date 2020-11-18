def decor(fun):
    def inner(n):
        result = fun(n)
        result = result + ", how are you?"
        return result
    return inner

@decor
def hello(name):
    return "Hello "+name

print(hello("Duncan"))