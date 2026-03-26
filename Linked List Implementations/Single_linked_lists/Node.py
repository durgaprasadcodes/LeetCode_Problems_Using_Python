class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def traversel(self):
        nodes=[]
        temp=self.head
        while temp:
            nodes.append(temp.data)
            temp=temp.next
        return "->".join(map(str,nodes))
    
    def insertionAtBegining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        return 
    def insertionAtLast(self,data):
        if self.head is None:
            return self.insertionAtBegining(data)
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        return 
            
l1=LinkedList()
l1.insertionAtBegining(10)
l1.insertionAtLast(20)
l1.insertionAtLast(30)
l1.insertionAtLast(40)
l1.insertionAtLast(50)
print(l1.traversel())