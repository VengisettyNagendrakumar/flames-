import tkinter as tk
from PIL import Image, ImageTk
window=tk.Tk()
window.title("Flames")
window.geometry('600x600')
bg= ImageTk.PhotoImage(file="flame.jpg")
label =tk.Label(window, image = bg)
label.pack()
from tkinter import messagebox
def ans():
    name1=entry1.get()
    name2=entry2.get()
    name1=name1.replace(" ","")
    name2=name2.replace(" ","")
    name1=list(name1)
    name2=list(name2)
    if not name1 or not name2:
        messagebox.showwarning("Invalid","Try again")
    else:
        for x in name1:
            if x in name2:
                name1.remove(x)
                name2.remove(x)
        n=len(name1)+len(name2)
        l=["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        #r.shuffle(l)
        while len(l)>1:
            index=n%len(l)-1
            if index>=0:
                right=l[index+1:]
                left=l[:index]
                l=right+left
            else:
                l=l[:len(l)-1]
        
        msg="Relationship between "+entry1.get()+" and " +entry2.get()+" is : "+l[0]
        f=tk.Label(window,text=msg,font=("system-ui",13,"bold"),padx=15,pady=15,fg="orange",bg="black")
        f.place(x=75,y=250)
        
label1=tk.Label(window,text="Name1",font=("helvetica",10,"bold"))
label1.place(x=100,y=100)
entry1=tk.Entry(window,width=30,font=("system-ui",13,"italic"),fg="green",bg="pink")
entry1.place(x=160,y=100,height=30)

label2=tk.Label(window,text="Name2",font=("helvetica",10,"bold"))
label2.place(x=100,y=140)
entry2=tk.Entry(window,width=30,font=("system-ui",13,"italic"),fg="blue",bg="aqua")
entry2.place(x=160,y=140,height=30)
button=tk.Button(window,text="Get",width=8,height=1,command=ans,bg="#000066",fg="white",
                 activebackground="#00cc00",padx=5,pady=5,font=("Helvetica",10,"bold"))
button.place(x=250,y=180)
