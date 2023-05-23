n=int(input("enter a num"))
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
        if 1 in l:
            l.remove(1)
for j in range(1,n):
    if j*j in l:
        l.remove(j*j)
print(l)
print(len(l))


'''or
Number=int(input('Enter the Number:'))
sfn=[]
for i in range(1,Number):
    if Number%i==0:
        s=int(i**0.5)
        if s*s!=i:
            sfn.append(i)
print(sfn)
print(len(sfn))
'''
    
