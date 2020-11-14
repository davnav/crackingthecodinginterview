# If the stack gets too high, it might topple. There-
# fore, in real life, we would likely start a new stack when the previous stack exceeds
# some threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
# Stacks should be composed of several stacks, and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
# behave identically to a single stack (that is, pop() should return the same values as it
# would if there were just a single stack)

from stack import stack

class SetOfStacks:
    stacklist = []
    def __init__(self,value):
        self.capacity=5
        self.stacklist.append(stack(value))
    def push_setofstacks(self,value):
        count = 0
        value_pushed = False
        for i in self.stacklist:
            print(i.list)
            if i.stacklen() < 5:

                print(i.stacklen())
                self.stacklist[count].push(value)
                value_pushed = True
            count = count + 1 
        if value_pushed != True :
            self.stacklist.append(stack(value))
            
                
    def printstack(self):
        i=0
        for stack1 in self.stacklist:
            print(stack1[i].list)
            i +=1
        
s = SetOfStacks(10)
# print(s.push_setofstacks(20))
        
# def stack(value):
    
#     def __init__(self):
#         self.list.append(value)
   
#     def push(self,value):
#         self.list.append(value) 
#     def pop_stack(self):
#         self.list.pop()

# s = stack(10)    
s.push_setofstacks(20) 
s.push_setofstacks(30) 
s.push_setofstacks(40) 
s.push_setofstacks(50) 
s.push_setofstacks(60) 
s.push_setofstacks(70) 
s.push_setofstacks(80) 
s.push_setofstacks(90)
s.printstack()
# print(s)   
    