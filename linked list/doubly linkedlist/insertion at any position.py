class Nodex:
    def __init__(self,data=None,next=None,prev=None):
        self.next=next
        self.data=data
        self.prev=prev

class doubleLL:
    def __init__(self):
        self.head=None
    
    def finsertion(self,data2):
        if self.head is None:
            self.head = Nodex(data2)
            return
        new_node = Nodex(data2)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
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
        
    def length(self):
        c = 0
        ptr = self.head   
        while ptr:
            c += 1
            ptr = ptr.next
        return c
     
    def backwardPrint(self):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
            # 
        while ptr:
            print(f"{ptr.data} -->",end=" ")
            ptr = ptr.prev

    
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
        
if __name__=="__main__":
    obj=doubleLL()
    obj.finsertion(67)
    obj.finsertion(1)
    obj.finsertion(7)
    obj.finsertion(33)
    obj.finsertion(90)
    obj.print_forward()
  
    obj.backwardPrint()
    print()
    obj.insertionAtAny(645,4)
    obj.print_forward()
    # print(obj.length())
        