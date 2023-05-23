#Almost Isosceles Right Triangles

x=int(input("enter num"))
l=[]
c=0
k=[]
while(1):
    y=x+1
    z=int((x*x+y*y)**0.5)
    if(z*z==x*x+y*y):
        l=[x,y,z]
        break
    else:
        x=x+1
print(l)
for i in l:
    if(i%2==0):
        for j in range(1,i+1):
            if(i%j==0):
                k.append(j)
                c=c+1
print(k)
print(c)
                
        

        

