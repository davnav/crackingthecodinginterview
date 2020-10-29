#Basic Tree operations will be implemented here.datetime A combination of a date and a time.


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def create_node(element):
    return Node(element)
        
class BinaryTree:
    
    def __init__(self,root):
        self.root = root
    
    # @classmethod 
    def create(self):
        current = self.root
        while current.left != None:
            current = current.left 
            
        e1 = input("input a value for the Tree:")
        current.left = create_node(e1)
        
        current = self.root
        while current.right != None:
            current = current.right
      
        e2 = input("input a value for the Tree:")
        current.right = create_node(e2) 
    

root = Node(18)
tree = BinaryTree(root)
tree.create()
print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
    
tree.create()
# print(tree.root.value)
print(tree.root.left.left.value)
print(tree.root.right.right.value)
    
    
    
    
