class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=LinkedList()
n=Node(10)
L.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(50)
n2.next=n3
L.display()
