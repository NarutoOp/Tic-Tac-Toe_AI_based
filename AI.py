user = "X"
opponent = "O"


def evaluate(board):
    # winner = None

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
    
    if winner == opponent:
        return 10
    elif winner == user:
        return -10
    elif winner == None:
        return 0

def check_rows():
    #set up global variable
    row_1 = False
    row_2 = False
    row_3 = False
    if board[0] == board[1] == board[2] != "-":
        row_1 = True
    if board[3] == board[4] == board[5] != "-":
        row_2 = True
    if board[6] == board[7] == board[8] != "-":
        row_3 = True
    

    #return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
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
    diagonal_2 = board[2] == board[4] == board[5] != "-"
    
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


def minimax(board,isMax):
    board2 = board

    score = evaluate(board2)

    if score == 10:
        return score
    if score == -10:
        return score

    if "-" not in board2 :
        return 0
    
    if isMax == True:

        best = -1000
        
        for i in range(0,9,1):
            if board2[i] == "-":
                board2[i] = opponent
                
                best = max(best,minimax(board2,False))
                board2[i] = "-"
        
        return best
    elif isMax==False:
        best = 1000

        for i in range(0,9,1):
            if board2[i] == "-":
                
                board2[i] = user
            
                best = min(best,minimax(board2,True))

                board2[i] = "-"
        return best


def findbestmove(board):
    bestval = -1000
    pos = -1
    board1 = board
    for i in range(0,9,1):
        if board1[i] == "-":
            
            board1[i] = opponent

            moveval = minimax(board1,False)

            board1[i] = "-"

            if moveval>bestval:
                pos = i
                bestval = moveval
                if bestval == 10:
                    break

    print("The value of best move is ",bestval)
    return pos

board = ["X","-","-",
         "-","-","-",
         "-","-","-"]
# board[7] = "X"
# v = minimax(board,True)
# print(v)
print(findbestmove(board))
# print(evaluate(board))
