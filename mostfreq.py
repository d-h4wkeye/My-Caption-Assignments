def most_frequent(S):
    T=[]
    O={}
    for i in S:
        if i not in T:
            T.append(i)
    for i in range(0,len(T)):
        O[T[i]]=S.count(T[i])
    print(sorted([O.items(),O.keys()],reverse=True))

x=input("Enter a string")
most_frequent(x)
