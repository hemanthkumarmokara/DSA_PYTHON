class nodex:
    def __init__(self,data=None,next=None,prev=None):
        self.next=next
        self.data=data
        self.prev=prev

class doubleLL:
    def __init__(self):
        self.head=None
    
    def linsertion(self,data2):
        if self.head is None:
            self.head = nodex(data2)
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
            
        ptr.next = nodex(data2,None,ptr)
    def deletionAtAny(self,pos):
        if self.head is None:
            print("Linked list is empty")
        if pos>self.length() or pos<2:
            print("enter correct position")
            return
        ptr1 = self.head
        ptr2 = ptr1.next
        for i in range(pos-2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr2.next
        temp = ptr2.next
        temp.prev = ptr1
        ptr2.next = None
        ptr2.prev = None
        print(f"deleted item is {ptr2.data}")
        
       
        

    
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
    obj.linsertion(67)
    obj.linsertion(1)
    obj.linsertion(7)
    obj.linsertion(33)
    obj.linsertion(90)
    obj.print_forward()
    obj.deletionAtAny(1)
    
    obj.print_forward()
    obj.backwardPrint()
    print()
    # print(obj.length())
        