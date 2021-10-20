def player_input():

	"""
	OUTPUT= (Player 1 marker, Payer 2 marker)
	"""

	marker= ''

	while marker != 'X' and marker != 'O':
		marker= input('Player1: choose: X or O').upper()

	if marker == 'X':

		return ('X', 'O')
	else:
		return('O', 'X')


player1, player2= player_input()

print(player1)
print(player2)