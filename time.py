'''t=int(input("enter a time"))
if(t<=0 or t>24):
    print("invalid")
elif(t==0):
    print("12 AM")
else:
    pass
    
if(t<12):
    print(f"{t} AM")
    if(t==0 and t<5):
        print("Midnight")
    else:
        print("morn")
    
else:
    if(t==12):
        print("12 AM")
        print("midnight")
    else:
        print(f"{t-12} PM")
        if(t==13 and t<17):
            print("after noon")
        elif(t==17 and t<21):
            print("evng")
        elif(t==21 and t<12):
            print("night")
        else:
            pass
'''
t=int(input("enter time"))
if(t<0 or t>24):
    print("invalid")
else:
    if(t<12):
        if(t==0):
            print("12 AM midnight")
        elif(t==1 or t<5):
            print(f"{t} AM midnight")
        else:
            print(f"{t} AM morning")
    elif(t>12 and t<24):
        if(t==12):
            print(f"{t} PM afternoon")
        elif(t==13 or t<17):
            print(f"{t-12} PM afternoon ")
        elif(t==17 or t<21):
            print(f"{t-12} PM evng")
        elif(t==21 or t<24):
            print(f"{t-12} PM night")
        else:
            pass
    else:
        pass
           
