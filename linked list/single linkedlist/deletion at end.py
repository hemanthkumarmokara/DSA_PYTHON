
class Nodex:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        
        
    def ldeletion(self):
        ptr1=self.head
        ptr2=ptr1
        while(ptr1.next):
            ptr2=ptr1
            ptr1=ptr1.next
        ptr2.next=None
        print(f"\ndeleted item is {ptr1.data}")
        
    def linsertion(self,data2):
        if self.head is None:
            self.head=Nodex(data2,None)
            return
        itr=self.head
       # itr=ptr.next
        while(itr.next):
            itr=itr.next
            
        itr.next=Nodex(data2,None)
        
    def print(self):
        if self.head is None:
            print("Your LinkedList is empty")
            return
        ptr=self.head
        while(ptr):
            print(f"{ptr.data} -->",end="")
            ptr=ptr.next  

if __name__ == "__main__":
    obj=LinkedList()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.linsertion(99)
    obj.linsertion(60)
    obj.print()
    obj.ldeletion()
   # obj.ldeletion()
    obj.print()
             