#program to find extension of given file name
name=input("Enter Filename:")
for i in range(0,len(name)):
    if(name[i]=="."):
        if(name[i+1::1]=="py"):
            print("Python")
        elif(name[i+1::1]=="txt"):
            print("Textfile")
        elif(name[i+1::1]=="c"):
            print("C")
        elif(name[i+1::1]=="exe"):
            print("Executablefile")
            
        
        
