n=int(input("enter row size"))
m=int(input("enter column size"))
k=m*n
count=0
for i in range(k):
    j=int(input("enter matrix ele either 0 or 1"))
    if j==0:
        count=count+1
    else:
        continue
print(count)
