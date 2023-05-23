from itertools import permutations
n=input("enter n")
k=permutations(n,len(n))
for i in k:
    m="".join(i)
    print(m)
