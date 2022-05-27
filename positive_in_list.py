List=[]
n=int(input("Enter no of elements: "))
for i in range(0,n):
    e=int(input())
    List.append(e)
    
New=[]
for i in range(0,len(List)):
    if(List[i]>0):
        New.append(List[i])
print(New)
        
