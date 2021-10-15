# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb

"""
Functions and Methods Homework Solutions
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def ran_check(num, low, high):
	mylist= [low, high]

	low= min(mylist)
	high= max(mylist)

	if num in list(range(low, high)):
		print(f"{num} is in the range between {low} and {high}")
	else:
		print(f"{num} aint in the range bruh")

	


ran_check(5,2,7)


#solution


def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')



# Check
ran_check(5,2,7)