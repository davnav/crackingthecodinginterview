#rat-maze problem

# rat-maze problem is an example for 
# recursion and backtracking 
#   [[1,0,0,1],
#    [1,0,0,0],
#    [1,1,1,1],
#    [1,1,0,1]]

# if consider above 2D list as Maze where '1' as path ( allowed to jump )
# and 0 is a wall(not allowed to jump), then find a path from cell [0,0] to [3,3]
# if exists
# Note: rat is allowed to jump 1 step to the right or 1 step to the down

Maze = [[0,0,0,1],
        [1,1,0,0],
        [1,1,0,1],
        [0,1,1,1]]
path = []
def solve(row,col,Maze):
    
    if  Maze[0][0] == 0  and row ==0 and col ==0:
        print(path)
        return False
    elif Maze[0][0] == 1 and row == 0 and col == 0:
        path.append((row,col))
        
    
    if mazeboundary(row,col):
            print(path)
            return True
    
    
        
    else:     
            if col < 3: 
            #take all choices to jump
        
            #first , let us take right jump
        
                if Maze[row][col+1] == 1:
                    path.append((row,col+1))
                    if solve(row,col+1,Maze):
                        return True
                    path.pop()
            if row < 3: 
                #second choice, take the down jump
                if Maze[row+1][col] == 1:
                    path.append((row+1,col))
                    if solve(row+1,col,Maze):
                        return True
                    path.pop()
        

            return False


            
def mazeboundary(row,col):
    if row == 3 and col == 3:

        return True 
    else:
        return False    
    
solve(0,0,Maze)