import math
s=0
n=int(input("enter n"))
for i in range(n):
    j=i
    k=str(i)
    s=0
    while(j>0):
        r=j%10
        s=s+int(math.pow(r,len(k)))
        j=j//10
    if s==i:
        print(i,end=" ")
