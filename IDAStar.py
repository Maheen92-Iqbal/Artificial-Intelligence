    import ast
import time
import os 
import psutil 
import copy

state = [6,1,8,4,0,2,7,3,5]
goal_state = [0,1,2,3,4,5,6,7,8]
  
def find_row_column(state,n):
    
    for row in range(0,3):
        for col in range(0,3):
      
            if n == state[row][col]:
                
                return row,col
                
def manhattan_distance(state,goal):
    
    new_state = [state[i:i+3] for i in range(0,len(state),3)]
    new_goal = [goal[i:i+3] for i in range(0,len(goal),3)]
    
    result = 0
    for i in range(1,9):
 
        row1 = find_row_column(new_state,i)[0]
        col1 = find_row_column(new_state,i)[1]
        row2 = find_row_column(new_goal,i)[0]
        col2 = find_row_column(new_goal,i)[1]
        
        result = result + abs(row1-row2) + abs(col1-col2)
        
    return result
        
def move_up(tile):
   
   new_tile = tile.index(0)-3
   tile[tile.index(0)] = tile[new_tile]
   tile[new_tile] = 0

def move_down(tile):
     
   new_tile = tile.index(0)+3
   tile[tile.index(0)] = tile[new_tile]
   tile[new_tile] = 0
   
def move_right(tile):
    
   new_tile = tile.index(0)+1
   tile[tile.index(0)] = tile[new_tile]
   tile[new_tile] = 0
                
def move_left(tile):
    
   new_tile = tile.index(0)-1
   tile[tile.index(0)] = tile[new_tile]
   tile[new_tile] = 0
   

def isgoal(board):
    
    if(board == goal_state):
        
        return True
        
    else:
        
        return False
      

def get_key(value, dictionary):
        """find the key(s) as a list given a value"""
        for k,v in dictionary.items():
            for i in range(0,len(v)):
                if v[i][0] == value:
                    return [k,v[i][1]]

              
def IDAStarSearch(board,depth):
    
    search_depth = 0
    close_list = set() 
    open_list = []
    close_list.add(tuple(board))
    
    path_to_goal = {}
      
    while not isgoal(board):
        
      node_list = []
    
      if board.index(0) != 2 and board.index(0) != 5 and board.index(0) != 8:
         node = copy.copy(board)
         move_right(node)
         
         if not tuple(node) in close_list:
             
           if search_depth < depth:
               
             open_list.insert(0,(search_depth+1+manhattan_distance(node,goal_state),node,search_depth+1))
             close_list.add(tuple(node))
            
             node_list.insert(0,(node,'Right'))
             #print 'Up' + str(open_list)
      
              
      if board.index(0) != 0 and board.index(0) != 3 and board.index(0) != 6:
         node = copy.copy(board)
         move_left(node)
         
         if not tuple(node) in close_list:
             
           if search_depth < depth:
               
             open_list.insert(0,(search_depth+1+manhattan_distance(node,goal_state),node,search_depth+1))
             close_list.add(tuple(node))
            
             node_list.insert(0,(node,'Left'))
             #print 'Up' + str(open_list)
             
      if board.index(0) != 6 and board.index(0) != 7 and board.index(0) != 8:
         node = copy.copy(board)
         move_down(node)
         
         if not tuple(node) in close_list:
             
             
           if search_depth < depth:
               
             open_list.insert(0,(search_depth+1+manhattan_distance(node,goal_state),node,search_depth+1))
             close_list.add(tuple(node))
            
             node_list.insert(0,(node,'Down'))
             #print 'Up' + str(open_list)
                         
      if board.index(0) != 0 and board.index(0) != 1 and board.index(0) != 2:
          
         node = copy.copy(board)
         move_up(node)
         
         if not tuple(node) in close_list:
           
           if search_depth < depth:
               
             open_list.insert(0,(search_depth+1+manhattan_distance(node,goal_state),node,search_depth+1))
             close_list.add(tuple(node))
            
             node_list.insert(0,(node,'Up'))
             #print 'Up' + str(open_list)
      
      path_to_goal[repr(board)] = node_list
             
      open_list.sort(key = lambda queue: queue[0])
      
      lst =  open_list.pop(0)  
     
      search_depth = lst[2]
       
      board = lst[1]
      
      
      if len(open_list) == 0:
        
          break
    
    
    return (board,path_to_goal)
     
def result(board,goal):
    
    depth = 1
    
    y = IDAStarSearch(board,depth)
    
    while(y[0] != goal):
        
        depth = depth + 1
    
        y = IDAStarSearch(board,depth)
    
        print depth
    
    l = []
    goal_directions = []
    
    l.append(goal_state)
    x = get_key(goal_state,y[1])
    l.append(x[0])
    goal_directions.insert(0, x[1])
    
    #get the keys of the goal node towards the initial state and insert the directions as we need them from top to bottom
    #and we are tracing back from bottom to top.
    while(ast.literal_eval(x[0]) != state):
        
        x = get_key(ast.literal_eval(x[0]),y[1])
        l.append(x[0])
        goal_directions.insert(0, x[1])
                  
    print goal_directions
        