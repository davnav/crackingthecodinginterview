# Find the nth elemnt from last of a singly linked list

#simple Node class with "value" and "next_node" which is pointing the same type "Node" 
class Node:
    def __init__(self,value):
        self.value = value
        self.next_node = None

#creatig a class to make a head - head will be known as linkedlist        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,key):
        
        current = self.head
        while current.next_node != None:
             current = current.next_node

        if current.next_node == None:
            new_node = Node(key)
            current.next_node = new_node
            new_node.next_node = None
    
    # print("**********Solution1*************")    
    def findnthElementfromlast(self,n):
        current = self.head
        count = 0
        #second_ref = self.head
        
        while current.next_node != None: 
            
            if count == n:
                second_ref = self.head
            if count >= n:
                second_ref = second_ref.next_node
            
            current = current.next_node
            
            count +=1
        
        return second_ref.next_node.value 
            
        
            
        
             
        
    
  

        

#the function which can print the linked list if we pass the head        
def printList(head):
    node = head
    while node != None:
        print('node value:'+ str(node.value))
        node=node.next_node 
    
            
list1 = LinkedList()
list1.head = Node(12)

#linked list operation
#adding new element in the front

list1.push(10)
list1.push(11)
list1.push(21)
list1.push(22)
list1.push(23)
list1.push(24)
list1.push(25)
list1.push(26)
list1.push(27)



#printing the linked list before  removing the duplicate  
print("printing the linked list before  removing the duplicate")
printList(list1.head)  

  
print("printing the linked list nth element from last")
#  printing the linked list nth element from last
print(list1.findnthElementfromlast(3)) 

# list1.delete_element(90) 

# # assert list1 == [12,3,12,3]
# print("****after deleting*****")
# printList(list1.head)  

        