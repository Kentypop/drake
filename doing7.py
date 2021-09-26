def check_guest(mylist, guess):
	if mylist[guess] == 'O':
		print("Correct!")
	else:
		print("Wrong guess!")	
		print(mylist)