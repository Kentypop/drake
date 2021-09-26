def player_guess():

	guess= ''

	while guess not in ['0', '1', '2']:
		guess= input("Pick a number: 0,1 or 2 ")

	return int(guess)


player_guess()
