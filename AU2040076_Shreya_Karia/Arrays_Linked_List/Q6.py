#Shreya Karia AU2040076
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list: 
    def __init__(self):
        self.head = None

def lsrch(l_list,element):
    temp = l_list.head
    i = 1
    while temp != None:
        if temp.data == element:
            return i
        temp = temp.next
        i = i + 1
    return -1





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
print(lsrch(list,34))