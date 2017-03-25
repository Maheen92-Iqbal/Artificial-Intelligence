from random import randint
 
class PlayerAI(object):
     
     def __init__(self):
         
         self.direction = -1
         
     def getRandomValue(self):
         
         if randint(0,99) < 100*0.9:
             return 2
         else:
             return 4
             
     def Heuristic_function(self,grid):
         
         weight = [[7,6,5,4],[6,5,4,3],[5,4,3,2],[4,3,2,1]]
         summation = 0
         
         for row in range(4):
             for col in range(4):
                 summation = summation + (weight[row][col] * grid.board[row][col])
                 
         return summation
         
     def alphaBetaMixMaxAlgorithm(self,alpha,beta,depth,grid,player):
         
         if depth == 0:
             eval_func = self.Heuristic_function(grid)
             return [eval_func, -1]
             
         if player:
             
             moves = grid.AvailableMoves()
             
             if moves == []:
                 
                 return [alpha, self.direction]
                 
             for i in moves:
                 
                 gridcopy = grid.copy_grid()
                 gridcopy.move(i)
                 
                 value = self.alphaBetaMixMaxAlgorithm(alpha,beta,depth-1,gridcopy,False)
                 
                 if value[0] > alpha:
                     alpha = value[0]
                     self.direction = i
                      
                 if beta <= alpha:
                     break
             
             result = [alpha, self.direction]         
             return result
             
         else:
            
            cells = grid.AvailableCells()
            
            if cells == []:
                return result
                
            random_cells = cells[randint(0,len(cells)-1)]
           
            grid.board[random_cells[0]][random_cells[1]] = self.getRandomValue()
            
            value = self.alphaBetaMixMaxAlgorithm(alpha,beta,depth-1,grid,True)
              
            if value[0] < beta:
                beta = value[0]
                
            result = [beta, value[1]]
            return result
            
         
            
     def getmove(self,grid):
        
       
        output = self.alphaBetaMixMaxAlgorithm(-float('inf'),float('inf'),3,grid,True)
        
        print "Expected Score: ", output[0]
        print "Direction: ", output[1]
        
        return output[1]