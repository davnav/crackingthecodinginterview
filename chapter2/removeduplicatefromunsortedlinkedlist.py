# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?


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
        
    
    def delete_element(self,key):
        current = self.head
        while current.next_node != None and current.value != key:
            prev = current
            current = current.next_node
            
        if (current.next_node != None and current.value == key):
            prev.next_node  = current.next_node

        

#the function which can print the linked list if we pass the head        
def printList(head):
    node = head
    while node != None:
        print('node value:'+ str(node.value))
        node=node.next_node 
    
print("**********Solution1*************")    
def removeDuplicate(head):
    node = head
    #taking the first node as reference and compare it with rest of them
    while node != None:
        
        #taking the second node as head1 for imaginary list starting from second element
        head1 = node.next_node
        
        #taking the previous node for "head1"
        prev = node
        #traversing through the imaginary list starting from second element.
        # and increment it in the outer loop
        
        while head1 != None:
            
            #compare the node value and head1 (inner loop) values are same or not?     
            if node.value == head1.value:
                #if same, move the head1's next node to prev's next node
                #as we are no longer need head1 current value
                prev.next_node =  head1.next_node
            else:
                #if not same, move the current head1 to prev as we will be incremnt 'head1' soon
                #in the next step
                prev = head1 
            head1 = head1.next_node

        node = node.next_node
                
            
list1 = LinkedList()
list1.head = Node(12)

#linked list operation
#adding new element in the front

list1.push(10)
list1.push(11)
list1.push(21)
list1.push(22)
list1.push(22)
list1.push(22)


#printing the linked list before  removing the duplicate  
print("printing the linked list before  removing the duplicate")
printList(list1.head)  
removeDuplicate(list1.head)
  
print("printing the linked list after removing the duplicate")
#printing the linked list after  removing the duplicate  
printList(list1.head) 

# list1.delete_element(90) 

# # assert list1 == [12,3,12,3]
# print("****after deleting*****")
# printList(list1.head)  

        
    