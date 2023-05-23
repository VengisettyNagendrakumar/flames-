class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=ne
    def insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head  is None:
            print("empty list")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=sll()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
l.insert_beg(5)
l.insert_end(90)
l.insert_pos(3,67)
l.display()
