def display_board(board):

    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])



def space_check(board, position):

	return board[position] == ''



def full_board_check(board):

	for i in range(1,10):
		if space_check(board, i):
			return False

	#BOARD IS  FULL IF WE RETURN True
	return True



test_board = ['#','','','','','','','','','']



#print(space_check(test_board, 2))

print("@@@@@@@@@")

print(full_board_check(test_board))