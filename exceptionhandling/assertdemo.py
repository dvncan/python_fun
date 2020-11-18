
try:
    num = int(input("Enter an even number"))
    assert num%2 == 0, "You have entered an invalid input"
except AssertionError as obj:
    print(obj)
