m="abc"
for i in range(0,len(m)):
    for j in range(0,len(m)):
        for k in range(0,len(m)):
            if i==j or j==k or k==i:
                continue
            print(m[i]+m[j]+m[k])
