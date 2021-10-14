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


