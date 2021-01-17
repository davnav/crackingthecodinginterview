
#Simple parser to parse 1+2*3  or 1+2 or 3 
#
# This can be written as below grammer
# E -> T+E|n
# T  -> F*T|F
# F -> n
# n -> number

i = 0
exp = "1+3"

def parse(e):
    a = parseE()
    return a
      

def parseE():
    if i < len(exp):
        
        parseT()
        if peek("+"):
            consume()
            parseE()
    return True    


def parseT():
    parseF()
    if peek("*"):
        consume()
        parseT()

def parseF():
    if(isNumber(peek())):
        consume()
        

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
    i += 1

def isNumber(c):
    return c.isdigit

print(parse(exp))
 

   


    

        

    
