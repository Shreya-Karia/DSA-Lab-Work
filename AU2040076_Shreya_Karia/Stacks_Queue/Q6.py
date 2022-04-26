#Shreya Karia AU2040076
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        return self.head is None
    
    def _len_(self):
        return self.count
    
    def enqueueb(self,el):
        node = Node(el)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1
    
    def enqueuef(self,el):
        node = Node(el)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
        self.count += 1
  
    def dequeuef(self):
        assert not self.isEmpty(), "Connot dequeue an empty queue!"
        node = self.head
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next
        self.count -= 1
        return node.data
    
    def dequeueb(self):
        assert not self.isEmpty(), "Connot dequeue an empty queue!"
        temp = self.tail
        if self.head == self.tail:
            self.tail = None
            self.head = None
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            node.next = None
        self.count -= 1
        return temp.data
        




        

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

Q = Deque()

Q.enqueueb(19)
Q.enqueueb(40)
Q.enqueueb(11)
Q.enqueuef(50)
m = Q.dequeueb()
c = Q.dequeuef()
print(m,c) 









