def conv(t):
    if(t<0 or t>24):
        print("Invalid")
    elif(t==0):
        print("12 AM")
    elif(t==12):
        print("12 PM")
    else:
        for i in range(1,12):
            if(i==t):
                print(f"{t} AM")
        for j in range(13,24):
            if(j==t):
                t1=t-12
                print(f"{t1} PM")
    for i in range(0,4):
        if(t==i):
            print("midnight")
    for j in range(4,12):
        if(t==j):
            print("morning")
    for k in range(12,15):
        if(t==k):
            print("afternoon")
    for l in range(15,19):
        if(t==l):
            print("evening")
    for m in range(19,24):
        if(t==m):
            print("night")
    
t=int(input("enter time in 24 hour format: "))
conv(t)
