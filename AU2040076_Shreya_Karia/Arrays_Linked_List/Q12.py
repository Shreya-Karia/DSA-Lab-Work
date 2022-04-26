#Shreya Karia AU2040076
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class dlinked_list: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def printl(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data,end=" ")
            tmp = tmp.next
        return ""
    
    def tdubbly_append(self,element):
        temp = self.tail
        temp.next = Node(element)
        Node(element).prev = temp
        self.printl()
        return "Over"
        
    
    def dubbly_append(self,element):
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.next = Node(element)
                temp.next.prev = temp
                self.printl()
                return "Over"
            temp = temp.next
        
    def dubbly_remove(self,element):
        temp = self.head
        while temp != None:
            if temp.next.data == element:
                temp.next = temp.next.next
                if temp.next != None:
                    temp.next.prev = temp
                self.printl()
                return ""
            temp = temp.next
        return "No such element"



list = dlinked_list()
list.head = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
list.tail = a5
list.head.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a2.prev = list.head
a3.prev = a2
a4.prev = a3
a5.prev = a4

list.tdubbly_append(8)
print(" ")
list.dubbly_remove(8)


