#Shreya Karia AU2040076
class lQueue :

  # Creates an empty queue.
  def __init__( self ):
    self._qhead = None 
    self._qtail = None 
    self._count = 0

  # Returns True if the queue is empty.
  def isEmpty( self ):
    return self._qhead is None

  # Returns the number of items in the queue.
  def __len__( self ):
    return self._count

  # Adds the given item to the queue.
  def enqueue( self, item ):
    node = _QueueNode( item ) 

    if self.isEmpty() :
      self._qhead = node 
    else :
      self._qtail.next = node

    self._qtail = node
    self._count += 1

  # Removes and returns the first item in the queue.
  def dequeue( self ):
    assert not self.isEmpty(), "Cannot dequeue from an empty queue." 
    node = self._qhead

    if self._qhead is self._qtail :
      self._qtail = None

    self._qhead = self._qhead.next 
    self._count -= 1
    return node.item

  # Private storage class for creating the linked list nodes.
class _QueueNode( object ):
  def __init__( self, item ):
    self.item = item
    self.next = None


def radixsort(arr,num):
    bin = [-1]*10
    for k in range(10):
        bin[k] = lQueue()
    column = 1
    for d in range(num):
        for key in arr:
            digit = (key//column) % 10
            bin[digit].enqueue(key)
        i = 0
        for j in bin:
            while not j.isEmpty():
                arr[i] = j.dequeue()
                i += 1
        column *= 10
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
 

radixsort(arr,3)
print(arr)


"""
def countsort(arr,en):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(0,n):
        index = arr[i]//en
        count[index%10] += 1
    
    for i in range(1,n):
        count[i] += count[i-1]
     
    i = n - 1
    while i >= 0:
        index = arr[i] // en
        output[count[index%10]-1] = arr[i]
        count[index%10] -= 1
        i -= 1
    
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
    
def radixsort(arr):
    max1 = max(arr)
    en = 1
    while max1 / en > 1:
        countsort(arr,en)
        en *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
 

radixsort(arr)
print(arr)

"""    