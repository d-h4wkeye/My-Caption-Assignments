def most_frequent(S):
    T=[]
    O={}
    for i in S:
        if i not in T:
            T.append(i)
    for i in range(0,len(T)):
        O[T[i]]=S.count(T[i])
    o_sorted=sorted(O.items(),key=lambda u:u[1],reverse=True)
    print(o_sorted)
x=input("Enter a string")
most_frequent(x)
