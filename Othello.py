# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Wong Tsz Yin
# Student ID : 1155093245
# Email Addr : 1155093245@link.cuhk.edu.hk
# Ref: https://inventwithpython.com/chapter15.html
import sys
import random



class GameBoard:
    def __init__(self):
        self.board = None

    def init_gameBoard(self):
        self.board = []
        for i in range(8):
            self.board.append([' '] * 8)
        for x in range(8):
            for y in range(8):
                    self.board[x][y] = ' '
        #set init pos
        self.board[3][3] = 'X'
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'
        self.board[4][4] = 'X'
        

    def check_ending(self):
        # if there is step for anay disc to go, return False
       for i in range (8):
            for j in range (8):
                if GameBoard.is_valid(self.board,'X',i,j)!=False:
                        return False
       for i in range (8):
            for j in range (8):
                if GameBoard.is_valid(self.board,'O',i,j)!=False:
                        return False
       return True 
    # check if x,y are in bound
    def onBoard(x, y):     
        return x >= 0 and x <= 7 and y >= 0 and y <=7
    
    
    def check_legal_move(self,symbol):
	    #check if their is a legal move given symbol
        #return True or False
        for i in range (8):
            for j in range (8):
                if GameBoard.is_valid(self.board,symbol,i,j)!=False:
                    return True
        print("There is no valid move for Player %s."%symbol)

    def is_valid(board,symbol,input_row,input_col): 
        flip_tile = [] 
        #check if occupied or out of bound
        if board[input_row][input_col]!=' ' or not GameBoard.onBoard(input_row,input_col):
            return False
        
        if (symbol=='O'):
            opponent='X'
        else:
            opponent='O'    
            
        #if this dir is valid,check all directions for flipping     
        for x_dir, y_dir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            #start pos
            current_x, current_y = input_row, input_col
            #pos of first next disc
            current_x+=x_dir
            current_y+=y_dir
            
            if GameBoard.onBoard(current_x, current_y) and board[current_x][current_y] == opponent:
                #finding own disc pos
                while board[current_x][current_y]== opponent:
                    current_x+=x_dir
                    current_y+=y_dir
                    #out of bound
                    if not GameBoard.onBoard(current_x,current_y):
                        break
                    if board[current_x][current_y] == symbol: 
                        break

                if not GameBoard.onBoard(current_x,current_y):
                    continue
                
                if board[current_x][current_y] == symbol:
                    while True:
                        current_x-=x_dir
                        current_y-=y_dir
                        if current_x == input_row and current_y == input_col:
                            break
                        flip_tile.append([current_x,current_y])
        
        #save what to be flipped               
        if len(flip_tile) == 0:
            return False
        
        return flip_tile
        
    def check_winner(self):
        x_num=0
        o_num=0
        for i in range (8):
            for j in range (8):
                if self.board[i][j] == 'X':
                    x_num+=1
                if self.board[i][j] =='O':
                    o_num+=1
        return [o_num,x_num]

    def execute_flip(self, pos, symbol):

        flip_disc=GameBoard.is_valid(self.board,symbol,pos[0],pos[1])

        self.board[pos[0]][pos[1]] = symbol
        for x, y in flip_disc:
            self.board[x][y] = symbol

    def printGameBoard(self):
        LINE = '------------------------------------'
   
        print('  ', end=' ')
        for x in range(8):
            print('| %s' % (x+1), end=' ')
        print('|')
        print(LINE)
        for y in range(8):
            print(' %s' % (y+1), end=' ')
            for x in range(8):
                print('| %s' % (self.board[x][y]), end=' ')
            print('|')
            print(LINE)

class Player:



    def __init__(self, symbol):
        self.playerSymbol = symbol

    def nextMove(self, board):
        pass

class Human(Player):
    def nextMove(self,board):
       valid_input = '1 2 3 4 5 6 7 8'.split() 
       input_col, input_row=input("Type the row and col to put the disc: ").split(' ')
       if (input_row in valid_input and input_col in valid_input):
           input_row=(int)(input_row)-1
           input_col=(int)(input_col)-1
       else:
            print("Invalid Input")
            return False

       if (not GameBoard.is_valid(board,self.playerSymbol,input_row,input_col)):
           print("Invalid Input")
           return False
       else:
           return [input_row,input_col]
		   
class Computer(Player):



    def nextMove(self,board):
        allMoves=Computer.getValidMoves(board,self.playerSymbol)
    #always occupy corner
        for i,j in allMoves:
            if Computer.isCorner(i,j):
                return [i,j]
    #win by luck  
        random.shuffle(allMoves)
        return(allMoves[0])
        
    def getValidMoves(board, symbol):
        validMoves = []
        for i in range (8):
            for j in range (8):
                if GameBoard.is_valid(board,symbol,i,j)!=False:
                    validMoves.append([i, j])
        return validMoves

    def isCorner(x, y):
        return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

class Othello:

    def __init__(self):
        self.gameBoard = GameBoard()
        self.player1 = None
        self.player2 = None
        self.turn = 0


    def createPlayer(self, symbol, playerNum):
        choice=0
        while (choice<1 or choice>2):
            print('Please choose player', playerNum ,'(%s):'%symbol)
            print('1. Human')
            print('2. Computer Player')
            choice=(int)(input("Your choice is: "))
        if (choice==1):
            print("Player", symbol,"is Human.")
            player= Human(symbol)
        elif (choice==2):
            print("Player", symbol,"is Computer.")
            player= Computer(symbol)
       
        return player  

    def startGame(self):
	    #basic logic
        self.player1 = self.createPlayer('O', 1)
        self.player2 = self.createPlayer('X', 2)

        self.gameBoard.init_gameBoard()
        self.gameBoard.printGameBoard()

       
        while not self.gameBoard.check_ending():
            current_player = [self.player1,self.player2][self.turn]
            #jump line handling
            if isinstance(current_player, Human):
                print("Player %s\"s turn."%current_player.playerSymbol,end=' ')
            else: 
                print("Player %s\"s turn."%current_player.playerSymbol)
                
            if self.gameBoard.check_legal_move(current_player.playerSymbol):                
                pos = current_player.nextMove(self.gameBoard.board)
                if (pos==False):
                    continue
                self.gameBoard.execute_flip(pos, current_player.playerSymbol)
            self.turn = 1 - self.turn
            self.gameBoard.printGameBoard()
        
        
        s1, s2 = self.gameBoard.check_winner()
        if s1 > s2:
            winner = 'O'  # Black
        elif s1 < s2:
            winner = 'X'  # White
        elif s1 == s2:
            winner = ' '  # Tie

        print('Count O : {}'.format(s1))
        print('Count X : {}'.format(s2))
        if winner != ' ':
            print('Player {} won!\n'.format(winner))
        else:
            print('A tie')


if __name__ == "__main__":
    othello = Othello()
    othello.startGame()
    
