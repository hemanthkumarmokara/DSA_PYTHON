
class Nodex:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertionAtAny(self,data,pos):
        if self.head is None:
            print(f"linked list is empty")
            return
        if pos>self.length() or pos<2:
            print(f"enter correct position")
            return
        
        ptr1 = self.head
        ptr2 = ptr1.next
        
        for i in range(pos-2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        new_node = Nodex(data,ptr2,ptr1)
        ptr1.next = new_node
        ptr2.prev = new_node
            
        
        
    def linsertion(self,data2):
        if self.head is None:
            new_node=Nodex(data2,None)
            new_node.next=new_node
            new_node.prev=new_node
            self.head=new_node
            return
        new_node=Nodex(data2,self.head)
        ptr = self.head.prev
        new_node.prev = ptr
        ptr.next=new_node
        self.head.prev = new_node
    
    def backwardPrint(self):
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
            

        # for i in range(9):
        for i in range(self.length()):
            print(f"{ptr.data} -->",end=" ")
            ptr = ptr.prev

    
        
    def print_forward(self):
        pr = self.head
     
        # for i in range(9):
        for i in range(self.length()):
            print(f"{pr.data} -->",end=" ")
            pr = pr.next        
    def length(self):
        if self.head is None:
            print(f"linkedlist is empty")
            return None            
        ptr = self.head
        c = 1
        while ptr.next != self.head:
            c += 1
            ptr = ptr.next
        return c+1
    
if __name__ == "__main__":
    obj=LinkedList()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.linsertion(33)
    obj.linsertion(6)
    # obj.print()
    obj.print_forward()
    print()
    obj.insertionAtAny(234,2)
    obj.print_forward()
    print()
    print(f"backward")
    obj.backwardPrint()
                 