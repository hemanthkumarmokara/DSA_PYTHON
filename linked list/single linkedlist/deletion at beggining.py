
class Nodex:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        
        
    def fdeletion(self):
        ptr=self.head
        self.head=ptr.next
        ptr.next=None
        print(f"deleted item is {ptr.data}")
        
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
            print("Linked list is empty")
            return
        ll=''                            
        ptr=self.head
        while ptr:
            ll += str(ptr.data) + "--> " 
            ptr=ptr.next
            #print(ll)
        print(ll)   

if __name__ == "__main__":
    obj=LinkedList()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.linsertion(99)
    obj.linsertion(60)
    obj.print()
    obj.fdeletion()
    #obj.fdeletion()
    obj.print()
             