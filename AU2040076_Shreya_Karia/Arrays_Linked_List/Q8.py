#Shreya Karia AU2040076
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list: 
    def __init__(self):
        self.head = None

def printl(list):
    tmp = list.head
    while tmp != None:
        print (tmp.data, end=" ")
        tmp = tmp.next

def linsatbeg(list,element):
    temp = list.head
    list.head = Node(element)
    list.head.next = temp
    printl(list)
    return "Over"
        
   


list = linked_list()
list.head = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
list.head.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
linsatbeg(list,8)