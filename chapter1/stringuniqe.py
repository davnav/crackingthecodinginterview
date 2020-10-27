#Implement an algorithm to determine if a string has all unique characters. What if you
#can not use additional data structures?
#

#***********Solution1**********
print("***********Solution1**********")

s = raw_input("enter an input value:")
l = len(s)
print(type(l))
    # s = s.sort()
# unique = True
    
def isUniqueStringSln1(s,l):
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

isUnique = isUniqueStringSln1(s,l)
print(isUnique)


#******Solution2****************
#below solution we are using a dictionary , not sure this violates the question as answer
#not supposed to use any other data structures
#I believe O(n) time complexicity and space complexcity is also O(n)
print("*****Solution2********")

def isUniqueStringSln2(s):
    table = {}
    unique = True
    for char in s:
        if char in table.keys():
            table[char] += 1
            print(table)
            unique = False
            break
        else:
            table[char] = 1
        
    return unique

isUnique = isUniqueStringSln2(s)
print(isUnique)

    
             





        
                
            
    