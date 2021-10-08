from random import shuffle


def shuffle_list(mylist):
	shuffle(mylist)

	return mylist


def player_guess():

	guess= ''

	while guess not in ['0', '1', '2']:
		guess= input("Pick a number: 0,1 or 2 ")

	return int(guess)


def check_guest(mylist, guess):
	if mylist[guess] == 'O':
		print("Correct!")
	else:
		print("Wrong guess!")	
		print(mylist)	



# INITIAL LIST
mylist= ['', 'O', '']

# SHUFFLE LIST
mixedup_list= shuffle_list(mylist)

# USER GUESS
guess= player_guess()

# CHECK GUESS
check_guest(mixedup_list, guess)