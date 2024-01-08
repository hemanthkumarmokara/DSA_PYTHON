class Nodex:
    def __init__(self,data,next):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
            
        return count
    
    def print(self):
        if self.head is None:
            print("Your LinkedList is empty")
            return
        ptr=self.head
        while(ptr):
            print(f"{ptr.data} -->",end="")
            ptr=ptr.next
    def linsertion(self,data2):
        if self.head is None:
            self.head=Nodex(data2,None)
            return
        itr=self.head
       # itr=ptr.next
        while(itr.next):
            itr=itr.next
            
        itr.next=Nodex(data2,None)
    def deletion_at_anyPos(self,index):
        if (index<0 or index>self.get_length()):
            raise Exception("Invalid syntax")
        c=1
        ptr1=self.head
        ptr2=ptr1
        while(c<index):
            ptr2=ptr1
            ptr1=ptr1.next
            c += 1
        ptr2.next=ptr1.next
        ptr1.next= None
        print(f"\ndeleted item is {ptr1.data}")
        
if __name__== "__main__":
    obj=LinkedList()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.linsertion(99)
    obj.linsertion(60)
    obj.print()
    obj.deletion_at_anyPos(3)
    obj.print()
    print(obj.get_length())