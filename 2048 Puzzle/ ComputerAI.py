from random import randint

class ComputerAI(object):
    
    def __init__(self):
        
        self.direction = (-1,-1)
     
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
             return eval_func 
             
         if player:
             
             cells = grid.AvailableCells()
             
             if cells == []:
                 return -1
             
             for c in cells:
                     
               gridcopy = grid.copy_grid()
             
               gridcopy.board[c[0]][c[1]] = self.getRandomValue()
             
               value = self.alphaBetaMixMaxAlgorithm(alpha,beta,depth-1,gridcopy,False)
             
               if value > alpha:
                 alpha = value
                 self.direction = c
               
               if beta <= alpha:
                 break
                 
             return alpha
             
             
         else:
            
            moves = grid.AvailableMoves()
            
            if moves:
                
                direction = moves[randint(0,len(moves)-1)]
                grid.move(direction)
                
                value = self.alphaBetaMixMaxAlgorithm(alpha,beta,depth-1,grid,True)
                
                if value < beta:
                    
                   beta = value
                   
            return beta
            
             
    def getmove(self,grid): 
            
        output = self.alphaBetaMixMaxAlgorithm(-float('inf'),float('inf'),3,grid,True)
        
        print "Expected Score: ", output
        
        return self.direction
