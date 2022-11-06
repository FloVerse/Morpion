from morpion import Morpion
game = Morpion()
game.create_board()

""""dz
i =2
for row in game.board :
    row[i] = 'X'
    i-=1
"""
#game.display()
#game.entry(0,0,'X')
#game.display()
game.start()

#test gain game.entry(0,1,'X') game.entry(1,1,'X') game.entry(2,1,'X')

#pip install pygame --pre