import random as rd
import re
from tracemalloc import start
from xmlrpc.client import Boolean
from Player import Player
import pygame

class Morpion : 
    def __init__(self) -> None:
        self.board = []
        

    def create_board(self) : 
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    
    def is_full(self) -> Boolean : 
        for row in self.board : 
            for case in row : 
                if case == '-' : return False
        return True
        
    def draw(self) -> Boolean :
        bool = False 
        for row in self.board : 
            if row.count("-") == 0 :
                bool = True
            else :
                bool = False
        return bool

    def is_win(self) -> Boolean : 
        #ligne
        for row in self.board :
            if row.count("X") == 3 or row.count("O") == 3 : return True #Si le nb d'occurences d'un poubt est egale à 3 renvoie true



        #colonnes
        col = []
        for j in range(3) : #1
            for i in range(3) :
                col.append(self.board[i][j])
            if col.count("X") == 3 or col.count("O") == 3 : return True
            col.clear()

        #diagonales
        diag = []
        count = 0
            #1er cas
        if self.board[0][0] == 'O' or self.board[0][0] == 'X' : 
                for i in range(3) :
                    diag.append(self.board[i][count])
                    count+=1
                if diag.count("X") == 3 or diag.count("O") == 3 : return True
                diag.clear()

                #2ème cas
        diag = []
        count = 0
        if self.board[0][2] == 'O' or self.board[0][2] == 'X' : 
                for i in range(3)[::-1] :
                    diag.append(self.board[i][count])
                    count+=1
                if diag.count("X") == 3 or diag.count("O") == 3 : return True
                diag.clear()

        return False



    def display(self) :
        for row in self.board : print(row)

    def entry(self,row,col,carac) -> Boolean :
        if row > 2 or col > 2 : return False
        self.board[row][col] = carac
        

    def start(self) :
        countP1 = 0
        countP2 = 0 
        p1 = Player('X',r"C:\Users\flori\Documents\Morpion-1\morpion\img\cross.png")
        p2 = Player('O',r"C:\Users\flori\Documents\Morpion-1\morpion\img\circle.png")
        
        pygame.init()
        pygame.display.set_caption("Morpion")
        window = pygame.display.set_mode((442, 437))
        #window.fill((0,0,0))
        grid = pygame.image.load(r'C:\Users\flori\Documents\Morpion-1\morpion\img\grid.png').convert_alpha()
        cross = pygame.image.load(p1.getImg()).convert_alpha()
        circle = pygame.image.load(p2.getImg()).convert_alpha()
        window.blit(grid, (0,0))

        clickable_areas = [pygame.Rect((69, 54), (85, 90)),
                           pygame.Rect((160, 54), (85, 90)),
                           pygame.Rect((265, 54), (85, 90)),
                           
                           pygame.Rect((69,150 ), (85, 90)),
                           pygame.Rect((160, 150), (85, 90)),
                           pygame.Rect((265, 150), (85, 90)),
                           
                           pygame.Rect((69, 244), (85, 90)),
                           pygame.Rect((160, 244), (85, 90)),
                           pygame.Rect((265, 244), (85, 90))]

        while self.is_win()==False and self.draw() == False :

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     stop = True
       
                elif event.type == pygame.MOUSEBUTTONUP :
                    pos = pygame.mouse.get_pos()
                    for area in clickable_areas : 
                        if area.collidepoint(pos):
                            self.entry(row,col,p1.getCarac())
                            self.display()
                            window.blit(
                                cross,
                                tuple(map(lambda i, j: i - j,area.center,(area.height/2,area.width/2)))
                            )



            pygame.display.update()


            """
            self.display()
            #Player 1 round
            if self.is_win() ==False and self.draw() == False :
                print("Player 1, that's your turn!\n")
                rowCH = input("Choose the row\n")
                row = int(rowCH)
                colCH = input("Choose the column\n")
                col = int(colCH)
                while row > 2 : row = int(input("Choose the row\n"))
                while col > 2 : col = int(input("Choose the column\n"))
                self.entry(row,col,p1.getCarac())
                if self.is_win() :countP1+=1

            self.display()
            #Player 2 round
            if self.is_win() ==False and self.draw() == False :
                print("Player 2, that's your turn!\n")
                rowCH = input("Choose the row\n")
                row = int(rowCH)
                colCH = input("Choose the column\n")
                col = int(colCH)
                while row > 2 : row = input("Choose the row")
                while col > 2 : col = input("Choose the column")
                self.entry(row,col,p2.getCarac())
                if self.is_win() : countP2+=1
        """    
        if self.draw() == True:
            self.display()
            print("Draw !")  
        elif countP1 == 1 :
            print("Player 1 wins this game !")
        elif countP2 == 1 :
            print("Player 2 wins this game !")
        pygame.quit()


