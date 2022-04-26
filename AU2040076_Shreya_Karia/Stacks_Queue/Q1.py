#Shreya Karia AU2040076
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def isEmpty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek in empty stack."
        return self.top.value
    
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack" 
        n = self.top
        self.top = self.top.next
        self.size -= 1
        return n.value
    
    def push(self,el):
        n = Node(el,self.top)
        n.next = self.top
        self.top = n
        self.size = self.size + 1


    
class Node:
    def __init__(self,value,link):
        self.next = None
        self.value = value
        self.next = link
        
s = Stack()
s.push(25)
s.push(24)
s.push(13)  
s.push(2230)
print(s.pop())
print(s.peek())