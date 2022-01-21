from random import shuffle

mylist= ['O','','']



def shuffling(mylist):
	
	shuffle(mylist)

	return mylist



def asking():

	guess= input("type in 0,1,2")

	while guess not in ['0','1','2']:
		guess= input("type again, 0,1,2")

	return int(guess)



def game(mylist_f, asking_f):

	if mylist[asking_f] == "O":
		print("congarts aye")
	
	else:
		print("Wrong mate")
		print(mylist)



#Shuffle
mylist_f= shuffling(mylist)

#Ask
asking_f= asking()


#Check
game(mylist_f, asking_f)






