#Shreya Karia AU2040076
#Refrence - Geeks For Geeks
class BST:
    data = 0
    left = None
    right = None
    
    def __init__(self, rvalue):
        self.data = rvalue
        self.left = None
        self.right = None
    
    def insert(self, value):
        curr = self
         
        while(True):
            if value< curr.data:
                if curr.left == None:
                    Tree_new = BST(value)
                    curr.left = Tree_new
                    return
                else:
                    curr = curr.left
            elif value > curr.data:
                if curr.right == None:
                    node_new = BST(value)
                    curr.right = node_new
                    return
                else:
                    curr = curr.right
            else:
                print("Value already exists.")
                return
    
    def getprecessor(self, rnode):
        curr = rnode
        while( curr.right != None):
            curr = curr.right
        
        return curr.data
    
    def getsuccessor(self, rnode):
        curr = rnode
        while (curr.left != None):
            curr = curr.left
        
        return curr.data
    
    def remove(self, value):
        curr = self
        prev = self
        if self == None:
            return
        while(True):
            if value < curr.data:
                if curr.left == None:
                    print("Value not present in the tree.")
                    return
                else:
                    prev = curr
                    curr = curr.left
            elif value > curr.data:
                if curr.right == None:
                    print("Value not present in the tree.")
                    return
                else:
                    prev = curr
                    curr = curr.right
            else:
                if curr.left == None and curr.right == None:
                    if curr == prev.left:
                        prev.left = None
                        return
                    else:
                        prev.right = None
                        return
                elif curr.left != None:
                    n_value = self.getprecessor(curr.left)
                    self.remove(n_value)
                    curr.data = n_value
                    return
                else:
                    n_value = self.getsuccessor(curr.right)
                    self.remove(n_value)
                    curr.data = n_value
                    return
    
    def p_tree(self, r_node):
        curr = r_node
        if curr == None:
            return
        else:
            self.p_tree(curr.left)
            print(curr.data, end = ", ")
            self.p_tree(curr.right)
    
    def Tree_print(self):
        if self == None:
            return
        curr = self
        self.p_tree(curr.left)
        print(curr.data, end = ", ")
        self.p_tree(curr.right)
        


b = BST(10)
b.insert(29)
b.insert(19)
b.insert(11)
b.insert(94)
b.insert(20)
b.insert(100)
b.insert(8)
b.insert(82)
b.insert(43)

b.Tree_print()

b.remove(29)
b.remove(19)
print(" ")
print("Modified Tree:")
b.Tree_print()
        
                    
                        
                    
                
        
            
            
        