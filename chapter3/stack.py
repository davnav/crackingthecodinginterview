# Build a stack and build pop and push methods

class stack:
    list = []
    def __init__(self,*args):
        self.list.append(args[0]) 
    
    def push(self,element):
        self.list.append(element)
        # print(self.list)
    
    def pop_stack(self):
        return self.list.pop()
    def stacklen(self):
        return len(self.list)


# my_stack = stack(30)   

# my_stack.push(10)     
# my_stack.push(80)     
# my_stack.push(90)     
# print(my_stack.pop_stack())
# print(my_stack.pop_stack())
# print(my_stack.pop_stack())