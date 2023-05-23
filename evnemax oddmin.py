l=[1,2,3,4,5,6,7,8]
m=[]
p=[]
k=[]
for i in l:
    if i%2==0:
        m.append(i)
    else:
        p.append(i)
for i in range(len(l)):
    if len(p)>0 and len(m)>0:
        k.append(max(m))
        m.remove(max(m))
        k.append(min(p))
        p.remove(min(p))
print(k)
    
    
    
