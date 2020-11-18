import logging

logging.basicConfig(filename = "mylog.log", level = logging.DEBUG)



try:
    f = open("myfile.txt", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a/b
    logging.info("Division in progress")
    f.write("writing %d into file" %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("ZeroDivisionError")
else:
    print("you have entered a non zero number")
finally:
    f.close()
    print("File closed")    

print("code after exception")