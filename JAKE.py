def blackjack(a,b,c):
    
    if a+b+c <= 21:
        return a+b+c

    elif sum[a,b,c] > 21 and 11 in [a,b,c]:
        return a+b+c -10

    elif a+b+c > 21:
        return "BUST"

    else:
        print("hmmmm?????")


print(blackjack(5,10,11))

##solution 

def blackjack(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

#WHY 31?? use of if elif else


# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
LEVEL 2 PROBLEMS

SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 
and extending to the next 9 (every 6 will be followed by at least one 9).
 Return 0 for no numbers.
"""


def summer_69(aa):
    
    total= 0

    for f in aa:
        if f== 6 or f== 9:
            continue
        total+= f

    return total


print(summer_69([2, 1, 6, 9, 11]))


#SOLUTION
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        ##while not add, at this point add= False, therefore while not add  is while not False == True?
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([4, 5, 6, 7, 8, 9])) 




# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
CHALLENGING PROBLEMS

COUNT PRIMES: Write a function that returns 
the number of prime numbers that exist up to and including a given number
"""

num = 17


if num> 1:

	for f in range(2, num//2+1):

	    #If number is divisible by any number between 2 n num//2,
	    #its not prime number
	    if num%f == 0:
	        print(f"this {num}, {f} not prime number")
	        break

	else:
	    print(f"this {num}, {f} issss prime number!!!")


#SOLUTION

def count_primes(num):

	#Check for 0 or 1 input
	if num< 2:
		return 0

	#########
	# 2 or greater
	#########

	#Store prime numbers
	primes= [2]

	#Counter going yp to input num
	x= 3

	# x is going through every number up to input num
	while x<= num:
		#Check if x is prime
		for y in range(3,x,2):
			if x%y == 0:
				x+= 2
				break
		else:
			primes.append(x)
			x+= 2

	print(primes)
	return len(primes)


print(count_primes(7))


##### else statement

def player_input():

	"""
	OUTPUT= (Player 1 marker, Payer 2 marker)
	"""

	marker= ''

	while marker != 'X' and marker != 'O':
		marker= input('Player1: choose: X or O').upper()

	if marker == 'X':

		return ('X', 'O')
	#why does this get trigger only when marker == O ?? is it because of the while statement above?
	else:
		return('O', 'X')


print(player_input())