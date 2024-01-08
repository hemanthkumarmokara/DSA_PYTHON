class pop:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class non:
    def __init__(self):
        self.head = None
        
    def length(self):
        c = 0
        ptr = self.head
        while ptr:
            c += 1
            ptr = ptr.next
        return c
        
    def linsertion(self,data2):
        
        # lol = Nodex(data2,self.head)
        if self.head is None:
            self.head = pop(data2,self.head)
        else:    
            ptr = self.head
            while ptr.next:
                # print("kokl")
                ptr = ptr.next
            lol = pop(data2,None)
            ptr.next = lol
        
    def insertionAtAny(self,data2,pos):
        if self.head is None:
            self.head = pop(data,None)
        len = self.length()
        # len=6
        if pos>len:
            print("enter correct position")
            return
        ptr1 = self.head
        ptr2 = ptr1.next
        for i in range(pos-2):
            ptr1 = ptr1.next
            ptr2 = ptr1.next
        lol = pop(data2,ptr2)
        ptr1.next = lol
            
            
    def print(self):
        if self.head is None:
            print("linked list is empty")
        ptr = self.head
        while ptr:
            print(ptr.data,end="-->")
            ptr = ptr.next
            

    
if __name__ == "__main__":
    obj = non()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.insertionAtAny(99,4)
    obj.print()