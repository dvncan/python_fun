try:
    pwd = input("enter a password: ")
    
    if len(pwd) < 8:
        raise InvalidPasswordException()
    
except:
    print("Password length must be at least 8.")
    
else:
    print("Valid password")
    
