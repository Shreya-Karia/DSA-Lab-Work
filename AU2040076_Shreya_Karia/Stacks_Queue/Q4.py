#Shreya Karia AU2040076
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head is None
    
    def _len_(self):
        return self.count
    
    def enqueue(self,el):
        node = Node(el)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Connot dequeue an empty queue!"
        node = self.head
        if self.head == self.tail:
            self.tail = None
        self.head = self.head.next
        self.count -= 1
        return node.data

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None





Q = Queue()

Q.enqueue(19)
Q.enqueue(40)
Q.enqueue(11)
Q.enqueue(50)
m = Q.dequeue()
print(m) 

    