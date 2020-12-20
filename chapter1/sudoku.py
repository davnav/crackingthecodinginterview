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

def solve(col,row,board):
    if col >=9:
       # results.append(board[col][row])
        row = row+1
   
    if row >=9:
        return board

    for  value in range(1,10):
       
       if board[col][row] == 0:
            board[col][row] = value
            if IsvalidValue(col,row,board):
                solve(col+1,row,board)
   
    board[col][row] = 0

   
def IsvalidValue(col,row,board):
  
    #sudoku rule 1:
    #search for 3*3 area if find that value, it's invalid selection
    #eg: if col =2,row =2 
    #        0,1,2 are col values to search
    #        0,1,2 are row values to search
    #eg: if col = 5, row =7
    #       3*2 = 6 , 5 is below 6 , col area search should be 5,4,3
    #       3*2 = 6 , row is 7 , greater than 6, so the area for row should be 3*3=9 >(less) 8,7,6 
    #col-3
    area =[[0,1,2],[3,4,5],[6,7,8]]
    
    if board[col][row] != 0:
        x = board[col][row] 
        # area set 1
        # column first 3 columns to end of row
        if col < 3 and col >=0  and row < 3 and row >= 0:
               for i in range(0,2):
                   for j in range(0,2):
                       if board[i][j]== x:
                           return False
                        
         
        if col < 3 and col >= 0 and row < 6 and row >=3:
            
        if col < 3 and col >= 0 and row < 9 and row >=6:
            
        # area set 2 
        # column second set of 3 columns ( ie:col 3 to 5) to end of row   
        # column starts with index 0
        # row index also starts with idex 0
        
        if col <6 and col >=3 and  row < 3 and row >= 0:
        
        if col <6 and col >=3 and  row < 6 and row >= 3:
        
        
        if col <6 and col >=3 and  row < 9 and row >= 6:
              
            
        # area set 3 
        # column third set of 3 columns ( ie:col 6  to 8) to end of row   
        if col <9 and col >=6 and  row < 3 and row >= 0:
        
        if col <9 and col >=6 and  row < 6 and row >= 3:
        
        
        if col <9 and col >=6 and  row < 9 and row >= 6:
                  
            
            
        for i in area
        
        
          
            raise NotImplementedError
    