#attempt to solve sudoku in python

#it would be an example for recursion and backtracking
#example sudoku board below
board = [[0,0,0,2,6,0,7,0,1],
         [6,8,0,0,7,0,0,9,0],
         [1,9,0,0,0,4,5,0,0],
         [8,2,0,1,0,0,0,4,0],
         [0,0,4,6,0,2,9,0,0],
         [0,5,0,0,0,3,0,2,8],
         [0,0,9,3,0,0,0,7,4],
         [0,4,0,0,5,0,0,3,6],
         [7,0,3,0,1,8,0,0,0]]

# results = [[0]*9]*9

# print(results)


#solve is our function which is going to solve sudoku board and return board
#it is recursive function as we need to take each blank cell and find it a valid choice
#our choice is from number 1..9 
#if choice is wrong , means IsvalidValue fuction returns "False",
#we have blank that cell back to zero and choose another value until the function "IsvalidValue"
#returns "True"

def solve():
    
    emptycell = getemptycell()
    
    if emptycell:
   
        row,col = emptycell 
            # if solve(col,row,board):  
        for  value in range(1,10):
            # if board[row][col] == 0:
                    if IsvalidValue(col,row,value):
                        board[row][col] = value
                        if solve():
                            return True
                        board[row][col] = 0
    else:
        print(board)
        return True
    
    return False

def getemptycell():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None     
 
   
def IsvalidValue(col,row,value):
         
        # if board[row][col] !=0:
        #     return True
        x =  value 
        #choosen value is valid only if
        # areaCheck , columnCheck and rowCheck passes
        areaCheck_bool = areaCheck(col,row,x,board)
        columnCheck_bool = columnCheck(col,row,x,board)
        rowCheck_bool = rowCheck(col,row,x,board)
        
        if areaCheck_bool and columnCheck_bool and rowCheck_bool:
            return True
        else:
            
            return False 

    
        
        
        
# areaCheck function definition
# x is value of the cell choosen
#sudoku rule 1:
    #search for 3*3 area if find that value, it's invalid selection
    #eg: if col =2,row =2 
    #        0,1,2 are col values to search
    #        0,1,2 are row values to search
    #eg: if col = 5, row =7
    #       3*2 = 6 , 5 is below 6 , col area search should be 5,4,3
    #       3*2 = 6 , row is 7 , greater than 6, so the area for row should be 3*3=9 >(less) 8,7,6 
    #col-3
def areaCheck(col,row,x,board):
        # area set 1
        # column first 3 columns to end of row
        # if col < 3 and col >=0  and row < 3 and row >= 0:
        if  0 <= col < 3 and 0 <= row < 3: 
            for i in range(0,3):
                for j in range(0,3):
                    if board[j][i]== x :
                        return False
            return True
                        
         
        # if col < 3 and col >= 0 and row < 6 and row >=3:
        
        if 0 <= col < 3 and 3 <= row < 6:   
            for i in range(0,3):
                for j in range(3,6):
                    if board[j][i]== x :
                        # if j == col and i == row:
                        #     continue
                        return False
            return True
                       
        # if col < 3 and col >= 0 and row < 9 and row >=6:
        
        if 0 <= col < 3 and 6 <= row < 9:    
                for i in range(0,3):
                    for j in range(6,9):
                        if board[j][i]== x :
                        #    if j == col and i == row:
                        #     continue 
                           return False
                
                return True
        # area set 2 
        # column second set of 3 columns ( ie:col 3 to 5) to end of row   
        # column starts with index 0
        # row index also starts with idex 0
        
        # if col <6 and col >=3 and  row < 3 and row >= 0:
       
        if 3 <= col < 6 and 0 <= row < 3: 
                for i in range(3,6):
                    for j in range(0,2):
                        if board[j][i]== x :
                        #    if j == col and i == row:
                        #     continue
                           return False
                
                return True
                       
        if col <6 and col >=3 and  row < 6 and row >= 3:
        
                for i in range(3,6):
                    for j in range(3,6):
                        if board[j][i]== x:
                            # if j == col and i == row:
                            #    continue
                            return False
                
                return True
        
        if col <6 and col >=3 and  row < 9 and row >= 6:
              
                for i in range(3,6):
                    for j in range(6,9):
                        if board[j][i]== x :
                        #    if j == col and i == row:
                        #         continue
                           return False
                
                return True
            
        # area set 3 
        # column third set of 3 columns ( ie:col 6  to 8) to end of row   
        if col <9 and col >=6 and  row < 3 and row >= 0:
        
                for i in range(6,9):
                    for j in range(0,3):
                        if board[j][i]== x:
                        #    if j == col and i == row:
                        #     continue
                           return False
                
                return True
            
        if col <9 and col >=6 and  row < 6 and row >= 3 :
        
                for i in range(6,9):
                    for j in range(3,6):
                        if board[j][i]== x :
                            # if j == col and i == row:
                            #   continue
                            return False
                
                return True 
            
        if col <9 and col >=6 and  row < 9 and row >= 6:
                  
                for i in range(6,9):
                    for j in range(6,9):
                        if board[j][i]== x :
                        #    if j == col and i == row:
                        #     continue
                           return False
                
                return True
            

#columnCheck function definition
         
def columnCheck(col,row,x,board):
    for i in range(0,9):
        if board[i][col] == x :
            return False
    return True

#rowCheck function definition
def rowCheck(col,row,x,board):
    for j in range(0,9):
        if board[row][j] == x :
            return False
        
    return True
          

#print(board)
print(solve() )   