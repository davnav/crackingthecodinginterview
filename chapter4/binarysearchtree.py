#binary search tree insert node, traversal

class Node:
    #initialization method
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
#function for creatig a new node
def create_node(element):
    return Node(element) 

class BinarySearchTree:
    #initialization
    def __init__(self,root):
        self.root = root

    def addtotree(self,value):
        current = self.root
        prev = None
        while current != None:
            if current.value > value:
                prev = current
                current = current.left
            else:
                prev = current
                current = current.right
        
        if prev.value > value:
            prev.left = create_node(value)
        else:
            prev.right = create_node(value) 
    
def printBtree(root):
)
        current = root
       
        if current != None :
         
            printBtree(current.left)
        
            print(current.value)
     
            printBtree(current.right)
                 

root = Node(100)
btree = BinarySearchTree(root)

btree.addtotree(101)
btree.addtotree(104)
btree.addtotree(98)
btree.addtotree(109)
btree.addtotree(99)

#printing binary search tree in order format
printBtree(btree.root)