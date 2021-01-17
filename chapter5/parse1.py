
#Simple parser to parse 1+2*3  or 1+2 or 3 
#
# This can be written as below grammer
# E -> T+E|n
# T  -> F*T|F
# F -> n
# n -> number

i = 0
v = 0
exp = "1+3*4"

def parse(e):
    a = parseE()
    return a
      

def parseE():
    
    global i,exp,v
    if i < len(exp):
        parseT()
        if peek("+"):
            consume()
            # parseE()
            v = v + parseE()
        
    return v   


def parseT():
    global v
    v = int(parseF())
    if peek("*"):
        consume()
        v = v * parseT()
    return int(v)

def parseF():
    if(isNumber(peek())):
        value = consume()
        return value
    
        

def peek(c = ''):
    global i
    if i < len(exp):
        if c == '':
            return exp[i]
         
        if exp[i] == c:
            return True
    return False

def consume():
    global i
    prev = i
    i += 1
    return exp[prev]

def isNumber(c):
    try:
        return c.isdigit
    except:
        print("parsing failed - converting to digit")

print(parse(exp))
 

   


    

        

    
