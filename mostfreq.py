def most_frequent(S):
    T=[]
    for i in S:
        if i not in T:
            T.append(i)
    for i in range(0,len(T)):
        print(T[i],"=",S.count(T[i]))
    

    

x=input("Enter a string")
most_frequent(x)
