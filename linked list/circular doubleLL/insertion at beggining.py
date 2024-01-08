class nodex:
    def __init__(self,data=None,next=None,prev=None):
        self.next=next
        self.data=data
        self.prev=prev

class doubleLL:
    def __init__(self):
        self.head=None
    
    def finsertion(self, data2):
        if self.head is None:
            new_node = nodex(data2)
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return
        new_node = nodex(data2,self.head)
        new_node.prev = self.head.prev
        lol=self.head.prev
        self.head.prev = new_node
        lol.next = new_node
        self.head = new_node

        

        
    def backwardPrint(self):
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
            

        # for i in range(9):
        for i in range(self.length()):
            print(f"{ptr.data} -->",end=" ")
            ptr = ptr.prev

    
    def print_forward(self):
        ptr = self.head
    #  
        # for i in range(9):
        for i in range(self.length()):
            print(f"{ptr.data} -->",end=" ")
            ptr = ptr.next

    def length(self):
        if self.head is None:
            print(f"linkedlist is empty")
            return None            
        ptr = self.head
        c = 1
        while ptr.next != self.head:
            c += 1
            ptr = ptr.next
        return c+1
    
if __name__=="__main__":
    obj=doubleLL()
    obj.finsertion(67)
    obj.finsertion(1)
    obj.finsertion(7)
    obj.finsertion(33)
    obj.finsertion(90)
    obj.print_forward()
    print()
    obj.backwardPrint()
        