import csv

def write(info):
    fp=open("Student_info.csv","a")
    writer=csv.writer(fp)
    if fp.tell()==0:
        writer.writerow(["Name","Age","Contact No","Email"])
    writer.writerow(info)

A=True
i=1
while(A):
    Student_info=input("Enter student information in the format(Name Age Contact No Email)")

    info_list=Student_info.split(" ")
    write(info_list)
    print("Student",1,"Information is \nName:",info_list[0],"\nAge:",info_list[1],"\nContact_No:",info_list[2],"\nEmail:",info_list[3])
    i+=1

    Check=input("Do you want to enter information for another student?(y/n)")
    if(Check=="y"):
        A=True
    elif(Check=="n"):
        A=False
    else:
        print("Wrong input")
    
    
