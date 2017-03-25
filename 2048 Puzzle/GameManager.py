from Grid import Grid
from PlayerAI import PlayerAI
from ComputerAI import ComputerAI

from random import randint


(PLAYER,COMPUTER) = (0,1)
actionDic = {0:"UP", 1:'DOWN', 2:'LEFT', 3:'RIGHT'}

class GameManager:
    
     def __init__(self, size = 4):
         
         self.grid = Grid(size)
         self.computerAI = None
         self.PlayerAI = None
         self.over = False
         
     def setComputerAI(self, compAI):
	 self.computerAI = compAI

     def setPlayerAI(self, playerAI):
	 self.playerAI = playerAI

     def display(self):
        
        for cell in self.grid.board:
            
            print cell
            
     def getRandomValue(self):
         
         if randint(0,99) < 100*0.9:
             return 2
         else:
             return 4
             
     def insertRandomTile(self):
          tilevalue = self.getRandomValue()
          cells = self.grid.AvailableCells()
          random_cells = cells[randint(0,len(cells)-1)]
          self.grid.board[random_cells[0]][random_cells[1]] = tilevalue
     
                       
     def start(self):
         
         for i in range(2):
             self.insertRandomTile()
             
         self.display()
         
         turn = PLAYER
        
         while True:
             gridCopy = self.grid.copy_grid()
	     move = None

	     if turn == PLAYER:
	         
		print "Player's Turn"
		move = self.playerAI.getmove(gridCopy)
		#print actionDic[move]

		#validate move
		if move != None and move >= 0 and move < 4:
			if self.grid.isTileMovable([move]):
				self.grid.move(move)
				maxtile = self.grid.getMaxTile()		
			
	     else:
		  print "Computer's turn"
		  move = self.computerAI.getmove(gridCopy)
				
		  if self.grid.canInsert(move):
			self.grid.board[move[0]][move[1]] = self.getRandomValue()
		  
	     self.display()

             if maxtile == 2048:
                 break
	     
	     turn = 1 - turn
	         
	     
def main():
	gameManager = GameManager()
	playerAI  = PlayerAI()
	computerAI  = ComputerAI()
	
	#set AIs and displayer
	
	gameManager.setPlayerAI(playerAI)
	gameManager.setComputerAI(computerAI)
	# start the game!
	gameManager.start()


if __name__ == '__main__':
	main()