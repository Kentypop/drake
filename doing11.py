import random



def display_board(board):

    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])


test_board = ['#','X','','','X','','','X','','']



def player_input():

	choice= "wrong"

	print("Welcome to Tic Tac Toe!")

	#Repeat till its X or O
	while choice not in ['X', 'O']:

		choice= input("Player : Do you want to be X or O?")

		if choice not in ['X', 'O']:
			print("Sorry, its invalid.")

	return choice



def place_marker(board, marker, position):


	while position not in list(range(1,11)):

		position= int(input("Choose a position from 1-10. "))

		if choice not in list(range(1,11)):

			print("Invalid, choose again from 1-10")


	board[position]= marker

	return board



#place_marker(test_board,'$',8)
display_board(test_board)



def win_check(board, mark):
    
    if board[1] == mark and board[2] == mark and board[3] == mark:

    	return True

    elif board[4] == mark and board[5] == mark and board[6] == mark:

    	return True

    elif board[7] == mark and board[8] == mark and board[9] == mark:

    	return True

    elif board[2] == mark and board[5] == mark and board[8] == mark:

    	return True

    elif board[3] == mark and board[6] == mark and board[9] == mark:

    	return True

    elif board[1] == mark and board[4] == mark and board[7] == mark:

    	return True

    elif board[1] == mark and board[5] == mark and board[9] == mark:

    	return True

    elif board[3] == mark and board[5] == mark and board[7] == mark:

    	return True

    else:
    	print("hmmm")



def choose_first():
    
    num= random.randint(1,2)

    if num == 1:
    	print("player1 goes first")
    elif num == 2:
    	print("player2 goess first")
    else:
    	print("??????????")


choose_first()


def space_check(board, position):

	return board[position] == ''



def full_board_check(board):

	for i in range(1,10):
		if space_check(board, i):
			return False

	#BOARD IS  FULL IF WE RETURN True
	return True





    
    
