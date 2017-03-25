import ast
import time
import os 

state = [1,2,5,3,4,0,6,7,8]
goal_state = [0,1,2,3,4,5,6,7,8]
import copy

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
      
close_list = set()
 
def get_key(value, dictionary):
      
        for k,v in dictionary.items():
            for i in range(0,len(v)):
                if v[i][0] == value:
                    return [k,v[i][1]]

                  
def DepthFirstSearch(board):
    
    start_time = time.time()
    
    open_list = []
    path_to_goal = {}
    l = []
    goal_directions = []
    search_depth = 0
    expanded_nodes = 0
    close_list.add(tuple(board))
    cost = 1
    maximum_fringe = 0
    maximum_search_depth = 0
    
    while not isgoal(board):
           
      node_list = []
      expanded_nodes = expanded_nodes + 1
      
      if board.index(0) != 2 and board.index(0) != 5 and board.index(0) != 8:
         node = copy.copy(board)
         move_right(node)
         
         if not tuple(node) in close_list:
             open_list.insert(0,(copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth = search_depth
             close_list.add(tuple(node))
             node_list.insert(0,(node,'Right'))
             
      if board.index(0) != 0 and board.index(0) != 3 and board.index(0) != 6:
         node = copy.copy(board)
         move_left(node)
         
         if not tuple(node) in close_list:
             
             open_list.insert(0,(copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth = search_depth
             close_list.add(tuple(node))
             node_list.insert(0,(node,'Left'))
        
                             
      if board.index(0) != 6 and board.index(0) != 7 and board.index(0) != 8:
         node = copy.copy(board)
         move_down(node)
         
         if not tuple(node) in close_list:
             
             open_list.insert(0,(copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth = search_depth
             close_list.add(tuple(node))
             node_list.insert(0,(node,'Down'))
        
      if board.index(0) != 0 and board.index(0) != 1 and board.index(0) != 2:
         node = copy.copy(board)
         move_up(node)
         
         if not tuple(node) in close_list:
             
             open_list.insert(0,(copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth = search_depth
             close_list.add(tuple(node))
             node_list.insert(0,(node,'Up'))
      
         
      path_to_goal[repr(board)] = node_list
     
      if maximum_fringe_size > maximum_fringe:
          maximum_fringe = maximum_fringe_size
            
        
      if max_depth > maximum_search_depth:
          maximum_search_depth = max_depth
      
      lst = open_list.pop(0)
     
      board = lst[0]
      search_depth = lst[1]
      
    end_time = time.time()
     
    l.append(goal_state)
    x = get_key(goal_state,path_to_goal)
    l.append(x[0])
    goal_directions.insert(0, x[1])
    
    #get the keys of the goal node towards the initial state and insert the directions as we need them from top to bottom
    #and we are tracing back from bottom to top.
    while(ast.literal_eval(x[0]) != state):
        
        cost = cost + 1
        x = get_key(ast.literal_eval(x[0]),path_to_goal)
        l.append(x[0])
        goal_directions.insert(0, x[1])
        
    print('Path_to_goal: {} '.format(goal_directions))
    print('cost_of_path: {} '.format(cost))
    print('nodes_expanded: {} '.format(expanded_nodes))
    print('fringe_size: {} '.format(len(open_list)))
    print('max_fringe_size: {} '.format(maximum_fringe))
    print('search_depth: {} '.format(search_depth))
    print('max_search_depth: {} '.format(maximum_search_depth))
    print('running_time: {} '.format(end_time - start_time))
