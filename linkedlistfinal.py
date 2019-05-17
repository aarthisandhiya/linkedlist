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
        
        
    def deleteAtBeg(self):
        temp=self.head
        self.head=temp.nextt
        temp.nextt=None
    
    def deleteAtLast(self):
        temp=self.head
        prev=temp
        while temp.nextt!=None:
            prev=temp
            temp=temp.nextt
        if temp.nextt==None:
            prev.nextt=None 
    def insertAtMiddle(self):
        s=int(input())
        temp=self.head
        pos=1
        while pos<s:
            temp=temp.nextt
            pos=pos+1 
        val=int(input(" enter a value to insert "))
        NewNode=Node(val)
        NewNode.nextt=temp.nextt
        temp.nextt=NewNode
        
    def deleteAtMiddle(self):
        e=int(input())
        temp=self.head
        pos=1
        while pos<e:
            prev=temp
            temp=temp.nextt
            pos=pos+1 
        prev.nextt=None
        prev.nextt=temp.nextt
    def search(self):
        print(" enter a value to be srarched")
        k=input()
        temp=self.head
        while temp.next!=None:
            if temp.data==k:
                print("yes",k , "is found")
            else:
                temp=temp.nextt
        else:
            if temp.nextt==None:
                k=temp.data
                print("yes",k,"is found")
            else:
                print("no",k,"the element is not in the list")
        
sl1=sll()
ch=0

while ch!=10:
    print("1.Insertion at the begining  2.insertion at middle 3.display 4.Insert  at end 5.deleteAtBeg 6.deleteAtENd 7.deleteAtMiddle 8. search")
    ch=int(input())
   
    if ch==1:
        sl1.insertAtBeg()
        sl1.display()
    elif ch==2:
        sl1.insertAtMiddle()
        sl1.display()
    elif ch==3:
        sl1.display()
    elif ch==4:
        sl1.insertAtEnd()
        sl1.display()
    elif ch==5:
        sl1.deleteAtBeg()
        sl1.display()
    elif ch==6:
        sl1.deleteAtLast()
        sl1.display()
    elif ch==7:
        sl1.deleteAtMiddle()
        sl1.display()
    elif ch==8:
        sl1.search()
    else:
        print("invalid choice")
    
