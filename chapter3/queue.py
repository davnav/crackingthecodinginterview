#build queue data structure and use push and pop methods
#**********************Solution1**************************
from collections import deque
class Queue:
    list = []
    def __init__(self):
        self.list = deque() 
    
    def push(self,element):
        self.list.append(element)
    
    def pop_queue(self):
        return self.list.popleft() 
   
queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
print(queue.pop_queue())
print(queue.pop_queue())
print(queue.pop_queue())

#***************Soluion2*****************
print("**********Solution2**********")

class QueueSln2:
    # list = []
    # front = 0
    # capacity = 0
    # rear = 0
    # size = 0
    
    def __init__(self,capacity):
        self.list = [None]*capacity
        self.front =0 
        self.capacity = capacity
        self.rear = capacity -1
        self.size = 0
        self.current = 0
        
    def push(self,element):
        if self.current < self.capacity:
            # print(self.list)
            self.list[self.current] = element
            self.current +=1 
        
    def pop_front(self):
        front_new = self.front
        # front_new = front_new+1
        self.front = self.front+1
        print(front_new)
        return self.list[front_new]
    
    def pop_rear(self):
        rear_new = self.list[self.rear]
        # print(rear_new)
        self.rear = self.rear -1
        return rear_new
    
    

que2 = QueueSln2(5)
que2.push(100)
que2.push(200)
que2.push(300)
que2.push(400)
que2.push(500)
        
# print(que2)        
print(que2.pop_front())        
print(que2.pop_rear())        