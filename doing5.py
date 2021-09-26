#section6 47
#import random
from random import shuffle


def shuffle_list(mylist):
	shuffle(mylist)

	return mylist


mylist= ['', 'O', '']

result= shuffle_list(mylist)	
print(result)
