# itertools.combinations(iterable, r)
# Return r length subsequences of elements from the input iterable.
# Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

#Example:
#  combinations('ABCD',2)   --> AB,AC,AD,BC,BD,CD
#  combinations(range(4),3) --> 012,013,023,123


#########Solutions 1 #######################
#This is for the below type of example where a list of 'n' numbers passed to find
#all combinations out of it

#  combinations([1,2,3],0,results,[])

import copy

def combinations(li,i,results,path1):
    

    
    if i == len(li):
        results.append(path1)
        return

    pathCurrent=copy.copy(path1)
    pathCurrent.append(li[i])
    print(pathCurrent)
    
    #find all combinations that  exclude the current item

    combinations(li,i+1,results,path1)
    
    #find all combination that include the current item
    combinations(li,i+1,results,pathCurrent)


li = [1,2,3]
i=0
path=[]
results=[[]]

combinations(li,i,results,path)

print(results)
