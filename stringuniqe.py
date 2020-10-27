#Implement an algorithm to determine if a string has all unique characters. What if you
#can not use additional data structures?
#



s = raw_input("enter an input value:")
l = len(s)
print(type(l))
    # s = s.sort()
# unique = True
    
def isUniqueString(s,l):
    unique = True 
    if l==0:
        print("enter a valid string")
        return False 
    if l >1:
        for i in range(0,l):
            if unique == True: 
                for j in range(i+1,l):
                    if s[i]== s[j]:
                        unique = False
                        break 
            else:
                break
        
        return unique

isUnique = isUniqueString(s,l)
print(isUnique)
        
                
            
    