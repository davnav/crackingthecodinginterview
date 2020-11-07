#Implement a function to check if a tree is balanced. For the purposes of this question,
#a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
# from the root by more than one.
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
    
def printBtree(root,inorder_list):

        current = root
       
        if current != None :
            
            print(current.value)
            # inorder_list.append(current.value)
            printBtree(current.left,inorder_list)
       
        
            # inorder_list.append(current.value)
            # print(current.value)
     
            printBtree(current.right,inorder_list)
            inorder_list.append(current.value)

# Check element in Binary Search Tree                 
def isElementFound(root,element):
    
    current = root
    found = False
    if current != None:
        if current.value == element:
            found = True
            return found
    
        if current.value > element:
            found = isElementFound(current.left,element)
        if current.value < element:    
            found = isElementFound(current.right,element)
    return found 

#Find element from Binary Search Tree    
#depth first search
def DFSFindElementPath(root,element,list1):
    
    current = root
    found = False
    list1 = list1
    if current != None:
        if current.value == element:
            list1.append(current.value)
            found = True
            return list1 
    
        else:
            if current.value > element:
                list1.append(current.value)
                list1 = DFSFindElementPath(current.left,element,list1)
            if current.value < element:    
                list1.append(current.value)
                list1 = DFSFindElementPath(current.right,element,list1)
    else:
        list1.pop()
        
    return list1 

#check whether a tree is balanced or not !

def isBalanced(root):
    current = root
    if current == None:
        return
    
     
    lh = height(current.left)
    rh = height(curent.right)
    
    if (lh-rh) <=1 and (lh-rh) >= -1 and isBalanced(current.left) 
        and isBalanced(current.left)
        return True
    
#find the height of a Tree

def height(root):
    current = root
    if current == None
        return 
    elif:
        lh = height(current.left) 
        rh = height(current.right)
        if lh > rh:
            return lh+1
        elif:
            return rh+1
    
        
   
root = Node(100)
btree = BinarySearchTree(root)

btree.addtotree(101)
btree.addtotree(104)
btree.addtotree(90)
btree.addtotree(88)
btree.addtotree(87)

btree.addtotree(109)
btree.addtotree(99)

#printing binary search tree in order format
# inorder_list = []
# # printBtree(btree.root,inorder_list)

# print(inorder_list)

list1=[]
print(isElementFound(btree.root,99))
print(DFSFindElementPath(btree.root,87,list1))