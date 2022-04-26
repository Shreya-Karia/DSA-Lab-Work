#Shreya Karia AU2040076
#Refrence - class notes
class Minheap:
    
    def __init__(self,maxsize):
        self.elements = [0]*maxsize
        self.count = 0
    
    def __len__(self):
        return self.count
    
    def capacity(self):
        return len(self.elements)
    
    def add(self, value):
        assert self.count < self.capacity(), "Cannot add to a full heap"
        self.elements[self.count] = value
        self.count += 1
        self.siftup( self.count -1)
    
    def extract(self):
        assert self.count > 0, "Cannot extract from an empty heap"
        value = self.elements[0]
        self.count -= 1
        self.elements[0] = self.elements[self.count]
        self.siftdown(0)
        return value
    
    def siftup(self, ndx):
        if ndx == 0:
            return
        if ndx > 0:
            parent = (ndx-1)//2
        if self.elements[ndx]< self.elements[parent]:
            self.elements[ndx], self.elements[parent] = self.elements[parent], self.elements[ndx]
            self.siftup(parent)
    
    def siftdown(self, ndx):
        left = 2*ndx + 1
        right = 2*ndx + 2
        
        smallest = ndx
        if left < self.count and self.elements[left] <= self.elements[smallest]:
            smallest = left
        if right < self.count and self.elements[right] <= self.elements[smallest]:
            smallest = right
        
        if smallest != ndx:
            self.elements[ndx], self.elements[smallest] = self.elements[smallest], self.elements[ndx]
            self.siftdown(smallest)
    
    
def Heapsort(list):
    n = len(list)
    heap = Minheap(n)
    for element in list:
        heap.add(element)
    for i in range(n):
        list[i] = heap.extract()
        


list = [12,87,34,16,45,29,11,37,18,95,120,59]
print(list)
Heapsort(list)
print(list)       