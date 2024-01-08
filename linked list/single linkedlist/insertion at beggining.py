#arrays store values at contiguous memory location
#where as linked list store values in random memory location
#Insert Element at beginning = O(1)
#Delete Element at beginning = O(1)
#Insert/Delete Element at the end/middle =O(n)

"""
Linked list has two main
benefits
over an array,
1.You don't need to pre-allocate space
2.insertion is easier
"""
class Nodex:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def finsertion(self,data2):
        nodex=Nodex(data2,self.head)
        self.head=nodex
        print(self.head)
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        ll=''                            
        ptr=self.head
        while ptr:
            ll += str(ptr.data) + "-->"
            ptr=ptr.next
        print(ll)   

if __name__ == "__main__":
    obj=LinkedList()
    obj.finsertion(76)
    obj.finsertion(79)
    obj.finsertion(46)
    obj.print()
             