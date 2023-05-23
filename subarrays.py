n=input("enter num")
l=[]
if len(n)<3:
    print("invalid input")
else:
    for i in range(len(n)+11):
        for j in range(i):
            k=n[j:i]
            if k not in l:
                l.append(k)
    print(l)
