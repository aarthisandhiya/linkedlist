class Node:
    def __init__(self,data):
        self.data=data 
        self.nextt=None
        
class sll:
    def __init__(self):
        self.head=None 
    def insertAtBeg(self):
        val=int(input("enter a value to insert "))
        NewNode=Node(val)
        NewNode.nextt=self.head
        self.head=NewNode
    def insertAtEnd(self):
        val=int(input("enter a value to insert "))
        NewNode=Node(val)
        if self.head is None:
            self.head=NewNode
            return
        temp=self.head
        while(temp.nextt):
            temp=temp.nextt
        temp.nextt=NewNode
            
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.nextt
         


sl1=sll()
ch=0

while ch!=5:
    print("1.Insertion at the begining  2.seletion st the begining 3.display 4.Insert  at end 5.exit")
    ch=int(input())
   
    if ch==1:
        sl1.insertAtBeg()
        sl1.display()
    elif ch==3:
        sl1.display()
    elif ch==4:
        sl1.insertAtEnd()
        sl1.display()
    else:
        print("invalid choice")
    
