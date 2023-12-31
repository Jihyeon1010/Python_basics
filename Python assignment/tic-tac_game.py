# function is print board format using below symbols
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

#difine check_winner function 
def check_winner(board):
    # Check rows if row in board
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    # Check columns if colums in board
    for col in range(3):
        if len(set(board[row][col] for row in range(3))) == 1 and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    #reture when none 
    return None

#difine function about board full situation
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

#define fucnction about tic_tac_toe
def tic_tac_toe():
    #difne empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    #first player
    current_player = 'X'
    
    #use loop while have winner
    while True:
        #represent board
        print_board(board)
        
        # define row and col and who enter the row and column
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        
        #if is board is row and col == '' and define winner = chech_winner(board)
        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            
            #if occur of winner print player X or O and break 
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            
            # if the arise fuction is_board_full print message and break
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            #if space not empty, print the below message
            print("That space is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()