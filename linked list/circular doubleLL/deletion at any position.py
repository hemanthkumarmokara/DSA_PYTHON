
class Nodex:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None
        
    def deletionAtAny(self,pos):
        if self.head is None:
            print(f"linkedlist is empty")
            return
        if pos>self.length() or pos<2:
            print(f"enter correct position")
            return
        ptr1 = self.head
        ptr2 = ptr1.next
        for i in range(pos - 2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr2.next
        lpr = ptr2.next
        lpr.prev = ptr1
        ptr2.next = None
        ptr2.prev = None
        
        
        print(f"deleted item is {ptr2.data}")
        
        
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
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        ll=''                            
        ptr=self.head
        while ptr:
            ll += str(ptr.data) + "--> " 
            ptr=ptr.next
            #print(ll)
        print(ll)   
        
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
    print()
    obj.print_forward()
    print()
    obj.deletionAtAny(1) 
    obj.print_forward()
    

    