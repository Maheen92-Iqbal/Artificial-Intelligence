from copy import deepcopy
from Grid_display import Grid_display

directionVector = (UPVEC, DOWNVEC, RIGHTVEC, LEFTVEC) = ((-1,0),(1,0),(0,1),(0,-1))
dirs = (up,down,right,left) = range(4)

class Grid(object):
    
    def __init__(self, size = 4):
        
        self.size = size
        self.board = [[0]*self.size for i in range(self.size)]
        
    def copy_grid(self):
        
        gridcopy = Grid()
        gridcopy.board = deepcopy(self.board)
        gridcopy.size = self.size
        return gridcopy
        
    def getcellvalue(self, (x,y)):
        
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            
            return None
            
        else:
            
            return self.board[x][y]
    
    def canInsert(self, pos):
        return self.getcellvalue(pos) == 0
        
    def getMaxTile(self):
        maxTile = 0
        for x in xrange(self.size):
            for y in xrange(self.size):
                maxTile = max(maxTile, self.board[x][y])
        return maxTile
        
    def move(self,position):
        
        if position == 0:
            return self.up()
        if position == 1:
            return self.down()
        if position == 2:
            return self.left()
        if position == 3:
            return self.right()
            
    def AvailableCells(self):
        
        availableCells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    availableCells.append((row,col))
                    
        return availableCells
        
    def AvailableMoves(self, position = dirs):
        
        availableMoves = []
        for row in range(self.size):
            for col in range(self.size):
                
                for m in position:
                    
                    gridcopy = self.copy_grid()
                    
                    if gridcopy.move(m):
                        availableMoves.append(m)
                        
        return availableMoves
                        
                                
    def isTileMovable(self, direction = dirs):
        
        position = set(direction)
        
        for row in range(self.size):
            for col in range(self.size):
                
                if self.board[row][col]:
                    
                    for i in position:
                        
                      move = directionVector[i]
                      
                      adj_board = self.getcellvalue((row + move[0], col + move[1]))
                
                      if adj_board == self.board[row][col] or adj_board == 0:
                          
                          return True
                          
                elif self.board[row][col] == 0:
                    
                    return True
                    
        return False
        
    def merge(self,board_set):
        
       if len(board_set) <= 1:
           return board_set
           
       i = 0
       while i < len(board_set)-1:
           
           if board_set[i] == board_set[i+1]:
               
              board_set[i] = board_set[i]*2
              
              del board_set[i+1]      
            
           i = i + 1
    
    def down(self):
        
        moved = False
        for row in range(self.size):
            lst = []
            
            for col in range(self.size-1,-1,-1):
                
                if self.board[col][row] != 0:
                    lst.append(self.board[row][col])
                    
            self.merge(lst)
            
            for col in range(self.size-1,-1,-1):
                
                value = lst.pop(0) if lst else 0
                
                if self.board[col][row] != value:
                    moved = True
                    
                self.board[col][row] = value
        
                        
        return moved
        
    def up(self):
        
        moved = False
        for row in range(self.size):
            lst = []
            
            for col in range(self.size):
                
                if self.board[col][row] != 0:
                    lst.append(self.board[row][col])
                    
            self.merge(lst)
            
            for col in range(self.size):
                
                value = lst.pop(0) if lst else 0
                if self.board[col][row] != value:
                    moved = True
                    
                self.board[col][row] = value
                
        return moved
        
    def right(self):
        
       moved = False
       for row in range(self.size):
           
           lst = []
           
           for col in range(self.size-1,-1,-1):
               
               if self.board[row][col] != 0:
                   lst.append(self.board[row][col])
                   
           self.merge(lst)
           
           for col in range(self.size-1,-1,-1):
                             
                value = lst.pop(0) if lst else 0
                if self.board[row][col] != value:
                    moved = True
                    
                self.board[row][col] = value
                
       return moved
        
    def left(self):
        
        moved = False
        for row in range(self.size):
            lst = []
        
            for col in range(self.size):
                
                if self.board[row][col] != 0:
                    lst.append(self.board[row][col])
                    
            self.merge(lst)
        
            for col in range(self.size):
                
                value = lst.pop(0) if lst else 0
                if self.board[row][col] != value:
                    moved = True
                    
                self.board[row][col] = value
                
        return moved
                    
