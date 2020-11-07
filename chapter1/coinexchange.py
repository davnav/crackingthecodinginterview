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
        # for l in range(length_list-1,-1,-1):
        for coin_value in coins:
            print(coin_value)
            if current_amount >= coin_value:
                # minDenominations(coins[0,l-1],amount)
            
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

def minDenominationsDP(coins,amount):
    for x in range(0,amount):
        for i in coins:     
            print(i)
    raise NotImplementedError        
