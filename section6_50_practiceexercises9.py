# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
LEVEL 2 PROBLEMS

BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
"""


def blackjack(a, b, c):
	total= a+ b+ c

	if total<= 21:

		return total
	elif total> 21 and 11 in (a,b,c) :

		total-= 10
		return total
	else:

		total= 'BUST'
		return total


print(blackjack(9,9,11))


#Solution
#it's wrong?

def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'