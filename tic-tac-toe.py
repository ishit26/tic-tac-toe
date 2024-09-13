#library import
import random


#TODO: code to display board

def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    
#TODO: code to choose marker 'X' or 'O'

def choose_marker():
    choice = ''
    while choice != 'X' and choice != 'O':
        choice = input('Player 1 choose your marker: ' + choice).upper
        if choice == 'X':
            return 'X', 'O'
        else:
            return 'O', 'X'
        
#TODO: code to position the marker choice in the board

def place_marker(board, marker, position):
    board[position] = marker
    
#TODO: code to which player should start game player 1 or player 2

def toss():
    flip = random.randint(0, 1) == 0
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'

#TODO: code to check the win condition

def win(board, marker):
    if((board[1] == marker and board[2] == marker and board[3] == marker) or 
       (board[4] == marker and board[5] == marker and board[6] == marker) or
       (board[7] == marker and board[8] == marker and board[9] == marker) or
       (board[1] == marker and board[4] == marker and board[7] == marker) or 
       (board[2] == marker and board[5] == marker and board[8] == marker) or
       (board[3] == marker and board[6] == marker and board[9] == marker) or
       (board[1] == marker and board[5] == marker and board[9] == marker )or
       (board[3] == marker and board[5] == marker and board[7] == marker)):
        return win(board, marker)

#TODO: code to check available space on board after player put his marker 

def space(board, position):
    return board[position] == ' '

#TODO: code to check weather board is full or not(Draw Condition)

def full_board(board):
    if "" in board: 
        return False
    else: 
        return True
    
#TODO: code to take input from player to put the marker on board using keyboard numpad

def player_choice(board):
    place = 0
    while place not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or space(board, place):
        place = int(input('Choose a position from numpad 1 to 9: '))
    return place
    
#TODO: code to if palyer want to play the game again

def replay():
    rep = ''
    while rep not in ['Y', 'N']:
        rep = input("Do you want to play again? Enter Y or N: ").upper()
    return (rep == 'Y')

print("----------------------------------------------")
print('Welcome to the Tic-Tac-Toe game')
print("----------------------------------------------")
# choose_marker()
# display_board(board)
# place_marker()
