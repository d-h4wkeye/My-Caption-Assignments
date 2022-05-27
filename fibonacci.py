#fibonacci series
n=int(input("Enter the limit"))
a=0
b=1
print(a)
print(b)
i=0
while(i<n):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
