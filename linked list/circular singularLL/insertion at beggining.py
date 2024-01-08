
class Nodex:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def finsertion(self,data2):
        if self.head is None:
            self.head = Nodex(data2)
            self.head.next = self.head
            return
        itr = self.head
        self.head = Nodex(data2,itr)
        lpr = itr
        while lpr.next != itr:
            lpr = lpr.next
        lpr.next = self.head
    
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
    obj=LinkedList()
    obj.finsertion(76)
    obj.finsertion(79)
    # obj.finsertion(46)
    # obj.finsertion(4)
    # obj.finsertion(2)
    obj.finsertion(12)
    obj.finsertion(58)
    obj.print()
    # obj.length()
             