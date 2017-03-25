import ast
import time
import os 
import psutil 
import copy

process = psutil.Process(os.getpid()) 

state = [1,2,5,3,4,0,6,7,8]
goal_state = [0,1,2,3,4,5,6,7,8]
  
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
        """find the key(s) as a list given a value"""
        for k,v in dictionary.items():
            for i in range(0,len(v)):
                if v[i][0] == value:
                    return [k,v[i][1]]

               
def BreadthFirstSearch(board):
    
    start_time = time.time()
    
    open_list = []
    path_to_goal = {}
    l = []
    goal_directions = []
    search_depth = 0
    max_depth = []
    expanded_nodes = 0
    close_list.add(tuple(board))
    cost = 1
    while not isgoal(board):
           
      node_list = []
      expanded_nodes = expanded_nodes + 1
      if board.index(0) != 0 and board.index(0) != 1 and board.index(0) != 2:
         node = copy.copy(board)
         move_up(node)
         
         if not tuple(node) in close_list:
             
             open_list.append((copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth.append(open_list[-1][1])
             close_list.add(tuple(node))
             node_list.append((node,'Up'))
                          
      if board.index(0) != 6 and board.index(0) != 7 and board.index(0) != 8:
         node = copy.copy(board)
         move_down(node)
         
         if not tuple(node) in close_list:
             
             open_list.append((copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth.append(open_list[-1][1])
             close_list.add(tuple(node))
             node_list.append((node,'Down'))
        
      if board.index(0) != 0 and board.index(0) != 3 and board.index(0) != 6:
         node = copy.copy(board)
         move_left(node)
         
         if not tuple(node) in close_list:
             
             open_list.append((copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth.append(open_list[-1][1])
             close_list.add(tuple(node))
             node_list.append((node,'Left'))
        
      if board.index(0) != 2 and board.index(0) != 5 and board.index(0) != 8:
         node = copy.copy(board)
         move_right(node)
         
         if not tuple(node) in close_list:
             open_list.append((copy.copy(node), search_depth+1))
             maximum_fringe_size = len(open_list)
             max_depth.append(open_list[-1][1])
             close_list.add(tuple(node))
             node_list.append((node,'Right'))
             
      path_to_goal[repr(board)] = node_list
     
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
    print('max_fringe_size: {} '.format(maximum_fringe_size))
    print('search_depth: {} '.format(search_depth))
    print('max_search_depth: {} '.format(max(max_depth)))
    print('running_time: {} '.format(end_time - start_time))   
    print('max_ram_usage: {} '.format((process.memory_info().rss)/float(2**20)))