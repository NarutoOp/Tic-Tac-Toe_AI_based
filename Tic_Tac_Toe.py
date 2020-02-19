#-------------------------------------------------------------------------------
# Name:       TicTac Toe
# Purpose:
#
# Author:      Arpit
#
# Created:     16-02-2020
# Copyright:   (c) zinga 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
#if game is going
game_still_going = True

#who won or tie
winner = None

#Whose turn is it

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    #display initial board
    display_board()

    #while game still going
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        #flip to the other player
        flip_player()
        #game has ended
    if winner == "X" or winner == "O":
            print(winner + " won.")
    elif winner == None:
            print("Tie.")

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9 :")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input, Choose a position from 1-9:")

        position = int(position) - 1
        if board[position] == "-" :
            valid = True
        else:
            print("you cant go there.Go agaim")


    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    #ste up global variable
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return winner
def check_rows():
    #set up global variable
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does have match, flag that there is win
    if row_1 or row_2 or row_3 :
        game_still_going = False
    #return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3 :
        return board[6]
    return
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if any column does have match, flag that there is win
    if column_1 or column_2 or column_3 :
        game_still_going = False
    #return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3 :
        return board[2]
    return
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    #if any diagonal does have match, flag that there is win
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    #return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board :
        game_still_going = False
    return
def flip_player():
    global current_player
    if current_player == "X" :
        current_player = "O"
    elif current_player == "O" :
        current_player = "X"
    return



play_game()
