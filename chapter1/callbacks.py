#create a callbacks list and make some basic operations like
#register a function and calling it etc.

class CallbacksV1:
    
    def __init__(self):
        self.callbacks = []
    
    def register(self,f):
        self.callbacks.append(f)
    
    def call(self,value):
        
        callback =  self.callbacks.pop()
            
        callback(value)

    
def add(x):
    print(x+1)

def add_two(x):
    print(x+2)
    return (x+2) 

c = CallbacksV1()
c.register(add)
c.register(add_two)

c.call(3)
c.call(5)