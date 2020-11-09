#minimum coin exchange problem
#coins of different denominations & Amount
#Find a minimum number of coins to make change of given amount 


#*********Solution1************
print("********greedy approch****soluion won't be accurate always***")
#we will see how to use greedy approch which may be not accuate alwaysdatetime A combination of a date and a time. Attributes: ()

#coins = { 1,5,6,9}
#amount to exhange = 11
#output = [5,6]

def minDenominations_wrong(coins,amount):
    
    current_amount = amount 
    #pick highest of the element from denominations 
    #sorting the list 
    coins.sort()
    #getting the length
    length_list = len(coins)
    #output of the function will be a list of denominations
    #initialize denominations   
    denominations = []
    
    #sum variable to match whether denominations sum reached target
    sum=0
    remain_sum=current_amount
    
    #greedy approch to get denominations
    #subtracting the amount each time  
    #But eventually we need to use 2 for loops
    
    for i in coins:
        for coin_value in coins:
            # print(coin_value)
            if current_amount >= coin_value:
            
                denominations.append(coin_value)
                current_amount = current_amount-coin_value
     
        #output of the function will be a list of denominations
        for coin in denominations:
            sum += coin
        remain_sum = amount-sum
        if remain_sum ==0:
            break
    return denominations
            
coins = [5,1,6,9]

print(minDenominations_wrong(coins,32))


#************Solutions using Dynamic programming ************
print("********Dynamic programming solution*******")

min_DP_matrix = []

def minDenominationsDP(coins,amount):
    coins.sort()
    print(coins)
    j=0
    for i in coins:
    # for x in range(0,amount-1):
        row = []
        for x in range(0,amount+1):     
            # print(i)
            
            if x < 1 :
                row.append(0)
            else:
                if x ==1  :
                    row.append(1)
                else:
                    if j ==0:
                        row.append(x)
                    else:
                        if (x-i) >= 0:
                           #formula for generating the table for minimum denominations 
                           min_val = min1(row[x-i] + 1,min_DP_matrix[j-1][x])
                           
                           #append the row with minimum value that we got
                           row.append(min_val)
                        else:
                            #if x-i <0 basically we can just copy the values from upper row
                            min_val = min_DP_matrix[j-1][x]
                            row.append(min_val)
        min_DP_matrix.append(row)
        
        j += 1

#function for finding the minimum from the passed values.
def min1(x,y):
    if x<y:
        return x
    else:
        return y
    
        
minDenominationsDP(coins,10)

print(min_DP_matrix)