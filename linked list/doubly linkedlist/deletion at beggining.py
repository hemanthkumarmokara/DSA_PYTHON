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
    def fdeletion(self):
        if self.head is None:
            print("there is nothing to delete")
        ptr = self.head
        self.head = ptr.next
        ptr.next = None
        self.head.prev = None
        print(f"deleted item is {ptr.data}")        
        
    
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
    obj.fdeletion()
    
    obj.print_forward()
    # obj.backwardPrint()
    print()
    # print(obj.length())
        