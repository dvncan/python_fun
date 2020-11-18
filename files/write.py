#open a file for writing
f = open("myfile.txt", "w")
print("Enter Text: (Type # when you are done)")

s=''
while s!='#':    
    #user input
    s = input()
    #write to file
    f.write(s+"\n")
    
f.close()

