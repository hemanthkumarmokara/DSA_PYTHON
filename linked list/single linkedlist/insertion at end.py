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
        self.ptr = None
    def linsertion(self,data2):
        
        # lol = Nodex(data2,self.head)
        if self.head is None:
            self.head = Nodex(data2,self.head)
        else:    
            ptr = self.head
            while ptr.next:
                # print("kokl")
                ptr = ptr.next
            lol = Nodex(data2,None)
            ptr.next = lol




    def print(self):
        if self.head is None:
            print("linked list is empty")
        ptr = self.head
        while ptr:
            print(ptr.data,end="-->")
            ptr = ptr.next 
    def length(self):
        c = 0
        ptr = self.head
        while ptr:
            c += 1
            ptr = ptr.next
        print(c)
if __name__ == "__main__":
    obj=LinkedList()
    obj.linsertion(76)
    obj.linsertion(79)
    obj.linsertion(46)
    obj.print()
    print()
    obj.length()
             