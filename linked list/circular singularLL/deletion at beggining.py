class Nodex:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def fdeletion(self):
        if self.head is None:
            print(f"print linkedlist is empty") 
            return
        itr = self.head
        self.head = itr.next 
        itr.next = None
        ptr = self.head  
        while ptr.next != itr:
            ptr = ptr.next
        ptr.next = self.head
        print(f"deleted item is {itr.data}")
    def linsertion(self,data2):
        if self.head is None:
            self.head = Nodex(data2)
            self.head.next = self.head
            return
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = Nodex(data2,self.head)
        
            
        
    def length(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        ptr = self.head
        # print("pop")
        c = 1
        while ptr.next != self.head:
            c += 1
            ptr = ptr.next        
        # print(c)
        return c 
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        ptr = self.head
        # print("pop")
        for i in range(self.length()+1):
        # for i in range(9):
            print(f"{ptr.data}",end=" --> ")
            # print("kok")
            ptr = ptr.next

if __name__ == "__main__":
    obj = LinkedList()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.linsertion(4)
    obj.print()
    print(f"")
    obj.fdeletion()
    obj.print()