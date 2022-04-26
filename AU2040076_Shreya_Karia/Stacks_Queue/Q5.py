#Shreya Karia AU2040076
# Refrence - Class Note
class PQueue:
    def __init__(self):
        self.head  = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.head is None
    
    def __len__(self):
        return self.size
    
    def enqueue(self,ele,pri):
        node = Node(ele,pri)
        
        if self.isEmpty() == True:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node
        self.size = self.size + 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self.head
        hp = node.priority
        hn = node
        while node != None:
            if node.priority < hp:
                hp = node.priority
                hn = node
                prevh = prevn 
            prevn = node
            node = node.next

        if self.size == 1: 
            self.tail = None
            self.head = None
            self.size = 0
        else:
            if hn is self.head:
                self.head = self.head.next 
            else:
                prevh.next = hn.next

            self.size -= 1

        return hn.item
    
    
    def prnpq ( self ):
        node = self.head
        while node != None:
            print(node.item,node.priority)
            node = node.next
    
    def printinorder(self):
        while not self.isEmpty() : 
            item = self.dequeue() 
            print(item)


class Node( object ):

    def __init__( self, item, priority ):
        self.item = item
        self.priority = priority
        self.next = None

mypql = PQueue()
mypql.enqueue( "purple", 5 )
mypql.enqueue( "black", 1 )
mypql.enqueue( "orange", 3 )
mypql.enqueue( "white", 0 )
mypql.enqueue( "green", 1 )
mypql.enqueue( "yellow", 5 )
mypql.prnpq()
print(mypql.dequeue())
print("The Priority Queue:")
mypql.printinorder()
